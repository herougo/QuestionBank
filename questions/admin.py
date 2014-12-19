from django.contrib import admin
from questions.models import Question, Solution, Source

admin.site.register([Question, Solution, Source])