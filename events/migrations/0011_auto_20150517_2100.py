# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0010_auto_20150515_0328'),
    ]

    operations = [
        migrations.AddField(
            model_name='outreachtrip',
            name='EAs_registered',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tour',
            name='EAs_registered',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
