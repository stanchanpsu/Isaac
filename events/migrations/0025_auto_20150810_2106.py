# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0024_event_total_eas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='EAs_needed',
            field=models.PositiveSmallIntegerField(default=0, null=True, editable=False, blank=True),
        ),
    ]
