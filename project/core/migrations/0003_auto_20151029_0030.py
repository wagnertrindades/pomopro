# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20151029_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timer',
            name='user',
            field=models.ForeignKey(verbose_name='Usuário', related_name='Timer', to=settings.AUTH_USER_MODEL),
        ),
    ]
