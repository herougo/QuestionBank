from datetime import datetime
from django.db import models
from django import forms
from django.contrib.auth.models import User


class ThreadForm(forms.Form):
    # Attach to view for users to create a thread
    def __init__(self, request):
        from questions.models import Question
        self.fields = (
            forms.CharField(field_name="Title", maxlength=128, is_required=True),
            forms.ChoiceField(field_name="Subject", choices=Question.SUBJECTS)
        )
        self.request = request

    def save(self, new_data):
        return Thread.objects.create_thread(
            self.request.user, new_data['Title'], new_data['Subject'])


class ThreadManager(models.Manager):
    def create_thread(self, user, title, subject=None):
        new_thread = self.model(title=title, creator=user,
                                upvotes=0, downvotes=0, date=datetime.today())
        new_thread.save()
        return new_thread


class Thread(models.Model):
    creator = models.ForeignKey(User)
    title = models.CharField(max_length=128)
    upvotes = models.PositiveSmallIntegerField()
    downvotes = models.PositiveSmallIntegerField()
    date = models.DateTimeField(editable=False)

    objects = ThreadManager()

    def __str__(self):
        return self.title + " (" + str(self.creator) + ")"

    def save(self):
        if not self.id:
            self.date = datetime.today()
        super(Thread, self).save()


class CommentForm(forms.Form):
    # Attach to view for users to comment
    def __init__(self, request):
        self.fields = (
            forms.TextField(field_name="Comment"),
            forms.ModelChoiceField(field_name="Thread",
                                   queryset=Thread.objects.all()),
        )
        self.request = request

    def save(self, new_data):
        return Comment.objects.create_comment(
            self.request.user, new_data['Comment'], new_data['Thread'])


class CommentManager(models.Manager):
    def create_comment(self, user, comment_text, thread):
        new_comment = self.model(comment_text=comment_text, creator=user,
                                 thread=thread, upvotes=0, downvotes=0,
                                 date=datetime.today())
        new_comment.save()
        return new_comment


class Comment(models.Model):
    comment_text = models.TextField()
    creator = models.ForeignKey(User)
    thread = models.ForeignKey(Thread)
    upvotes = models.PositiveSmallIntegerField()
    downvotes = models.PositiveSmallIntegerField()
    date = models.DateTimeField(editable=False)

    objects = CommentManager()

    def __str__(self):
        return self.creator.username[:20] + ": " + self.comment_text[:40]

    def save(self):
        if not self.id:
            self.date = datetime.today()
        super(Comment, self).save()