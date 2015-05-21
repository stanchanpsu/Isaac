# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0014_auto_20150521_1501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outreachtrip',
            name='EAs_registered',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='EAs_registered',
        ),
        migrations.DeleteModel(
            name='OutreachTrip',
        ),
        migrations.DeleteModel(
            name='Tour',
        ),
    ]
