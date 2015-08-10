# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0021_auto_20150803_1516'),
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
        migrations.AddField(
            model_name='event',
            name='EAs_registered',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='EAs_needed',
            field=models.PositiveSmallIntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='hours',
            field=models.DecimalField(default=0, null=True, max_digits=3, decimal_places=1, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='note',
            field=models.CharField(default=b'No additional notes', max_length=500, null=True, blank=True),
        ),
    ]
