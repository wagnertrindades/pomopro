# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('type', models.IntegerField(choices=[(0, 'Pomodoro'), (1, 'ShortBreak'), (2, 'LongBreak')], verbose_name='Tipo')),
                ('created_at', models.DateTimeField(verbose_name='Criado em', auto_now_add=True)),
                ('user', models.ForeignKey(verbose_name='Usuário', related_name='Pomodoros', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='pomodoro',
            name='user',
        ),
        migrations.DeleteModel(
            name='Pomodoro',
        ),
    ]
