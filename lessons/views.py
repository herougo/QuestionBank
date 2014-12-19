from django.shortcuts import render, get_object_or_404
from lessons.models import Lesson


def index(request):
    all_lessons = Lesson.objects.all()
    context = {'lesson_list': all_lessons}
    return render(request, 'lessons/index.html', context)


def lesson_template(request, lesson_id):
    l = get_object_or_404(Lesson, id=lesson_id)
    return render(request, 'lessons/lesson_template.html', {'lesson': l})