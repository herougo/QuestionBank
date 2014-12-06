from datetime import datetime
from django.db import models


class LessonManager(models.Manager):
    def create_lesson(self, user, title, text, subject=None):
        new_lesson = self.model(title=title, creator=user, lesson_text=text,
                                date=datetime.today())
        new_lesson.save()
        return new_lesson


class Lesson(models.Model):
    title = models.CharField(max_length=64, default="")
    lesson_text = models.TextField()
    date = models.DateTimeField(editable=False)

    def __str__(self):
        return self.title[:50]

    def save(self):
        if not self.id:
            self.date = datetime.today()
        super(Lesson, self).save()