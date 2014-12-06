from django.contrib import admin
from discussions.models import Thread, Comment

admin.site.register([Thread, Comment])