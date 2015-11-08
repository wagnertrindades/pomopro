# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20151029_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timer',
            name='user',
            field=models.ForeignKey(related_name='timer', verbose_name='Usuário', to=settings.AUTH_USER_MODEL),
        ),
    ]
