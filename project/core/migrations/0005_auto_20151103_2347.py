# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20151103_2030'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timer',
            old_name='type',
            new_name='status',
        ),
    ]
