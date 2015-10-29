# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pomodoro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(0, 'Pomodoro'), (1, 'ShortBreak'), (2, 'LongBreak')], verbose_name='Tipo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('user', models.ForeignKey(verbose_name='Usuário', to=settings.AUTH_USER_MODEL, related_name='Pomodoros')),
            ],
        ),
    ]
