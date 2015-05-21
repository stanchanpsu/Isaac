# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0017_auto_20150521_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='EAs_needed',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='hours',
            field=models.DecimalField(null=True, max_digits=3, decimal_places=1, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(max_length=140, null=True, blank=True),
        ),
    ]
