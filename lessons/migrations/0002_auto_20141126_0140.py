# encoding: utf8
from django.db import models, migrations
from django.conf import settings
import datetime
from django.contrib.auth.models import User


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='lesson_name',
            new_name='title',
        ),
        # migrations.AddField(
        #     model_name='lesson',
        #     name='creator',
        #     field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=User.objects.get(id=1), to_field=u'id'),
        #     preserve_default=False,
        # ),
        migrations.AddField(
            model_name='lesson',
            name='date',
            field=models.DateTimeField(default=datetime.date(2014, 11, 26), editable=False),
            preserve_default=False,
        ),
    ]
