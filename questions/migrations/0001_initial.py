# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Solution',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('solution_text', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('source_name', models.CharField(max_length=64)),
                ('source_url', models.CharField(max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_title', models.CharField(max_length=64)),
                ('question_text', models.TextField()),
                ('subject', models.CharField(default='MATH', max_length=5, choices=[('MATH', 'Mathematics'), ('PMATH', 'Pure Mathematics'), ('CS', 'Computer Science'), ('CO', 'Combinatorics and Optimization'), ('STAT', 'Statistics'), ('ACTSCI', 'Actuarial Science'), ('AMATH', 'Applied Mathematics')])),
                ('difficulty', models.CharField(default='M', max_length=1, choices=[('E', 'Easy'), ('M', 'Medium'), ('H', 'Hard')])),
                ('solution', models.ForeignKey(to_field=u'id', blank=True, to='questions.Solution', null=True)),
                ('source', models.ForeignKey(to_field=u'id', blank=True, to='questions.Source', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
