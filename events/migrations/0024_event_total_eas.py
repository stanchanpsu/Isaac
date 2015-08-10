# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0023_auto_20150810_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='total_EAs',
            field=models.PositiveSmallIntegerField(default=0, null=True, blank=True),
        ),
    ]
