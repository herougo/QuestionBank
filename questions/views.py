from django.shortcuts import render, get_object_or_404
from questions.models import Question


def index(request):
    all_questions = Question.objects.all()
    context = {'question_list': all_questions}
    return render(request, 'questions/index.html', context)


def question_template(request, question_id):
    q = get_object_or_404(Question, id=question_id)
    return render(request, 'questions/question_template.html', {'question': q})