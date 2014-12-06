from django.conf.urls import url
from discussions import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<discussion_id>[0-9]+)/$', views.thread_template, name='thread_template'),
]