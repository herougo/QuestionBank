from django.conf.urls import url
from lessons import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<lesson_id>[0-9]+)/$', views.lesson_template, name='lesson_template'),
]