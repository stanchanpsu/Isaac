# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groupme', '0006_auto_20150813_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='event',
            field=models.OneToOneField(null=True, default=None, blank=True, to='events.Event'),
        ),
    ]
