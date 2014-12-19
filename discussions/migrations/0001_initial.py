# encoding: utf8
from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Thread',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field=u'id')),
                ('title', models.CharField(max_length=128)),
                ('upvotes', models.PositiveSmallIntegerField()),
                ('downvotes', models.PositiveSmallIntegerField()),
                ('date', models.DateTimeField(editable=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
