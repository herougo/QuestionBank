# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('lesson_name', models.CharField(default='', max_length=64)),
                ('lesson_text', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
