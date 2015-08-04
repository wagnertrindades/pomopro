# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import project.core.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', project.core.models.CustomUserManager()),
            ],
        ),
    ]
