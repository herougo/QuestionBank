from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings


def home(request):
    from django.shortcuts import render
    return render(request, 'index.html', {})

urlpatterns = patterns(
    '',
    url(r'^$', home, name='home'),
    url(r'^home/', home, name='home'),
    url(r'^questions/', include('questions.urls')),
    url(r'^discussions/', include('discussions.urls')),
    url(r'^lessons/', include('lessons.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )