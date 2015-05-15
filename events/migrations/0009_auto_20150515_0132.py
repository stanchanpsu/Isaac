# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20150514_0137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outreachtrip',
            name='note',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tour',
            name='note',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
    ]
