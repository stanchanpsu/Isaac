# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groupme', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='groupme_id',
        ),
        migrations.AddField(
            model_name='group',
            name='group_id',
            field=models.PositiveIntegerField(default=0, blank=True),
        ),
    ]
