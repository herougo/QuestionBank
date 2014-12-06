from django.shortcuts import render
from discussions.models import Thread, Comment


def index(request):
    all_discussions = Thread.objects.all()
    context = {'discussion_list': all_discussions}
    return render(request, 'discussions/index.html', context)


def thread_template(request, discussion_id):
    comments = Comment.objects.filter(thread=discussion_id)
    title = Thread.objects.get(id=discussion_id).title
    context = {'comment_list': comments, 'title': title}
    return render(request, 'discussions/thread_template.html', context)