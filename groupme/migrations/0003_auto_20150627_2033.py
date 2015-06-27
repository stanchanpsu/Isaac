# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0019_auto_20150521_1754'),
        ('personal', '0012_auto_20150627_2033'),
        ('groupme', '0002_auto_20150627_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='event',
            field=models.OneToOneField(default=None, blank=True, to='events.Event'),
        ),
        migrations.AddField(
            model_name='group',
            name='image_url',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(to='personal.EngineeringAmbassador', blank=True),
        ),
    ]
