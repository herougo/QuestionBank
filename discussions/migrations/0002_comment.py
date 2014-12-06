# encoding: utf8
from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('discussions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_text', models.TextField()),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field=u'id')),
                ('thread', models.ForeignKey(to='discussions.Thread', to_field=u'id')),
                ('upvotes', models.PositiveSmallIntegerField()),
                ('downvotes', models.PositiveSmallIntegerField()),
                ('date', models.DateTimeField(editable=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
