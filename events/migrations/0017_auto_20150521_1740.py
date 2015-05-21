# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0016_event_outreachtrip_tour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='EAs_needed',
            field=models.PositiveSmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='hours',
            field=models.DecimalField(max_digits=3, decimal_places=1, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(max_length=140, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='outreachtrip',
            name='EAs_registered',
            field=models.ManyToManyField(related_name='outreach', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AlterField(
            model_name='tour',
            name='EAs_registered',
            field=models.ManyToManyField(related_name='tours', to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
