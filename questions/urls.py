from django.conf.urls import url
from questions import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', views.question_template, name='question_template'),
]