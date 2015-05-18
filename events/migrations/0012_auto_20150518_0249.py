# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_auto_20150517_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='EAs_registered',
            field=models.ManyToManyField(related_name='EA', to=settings.AUTH_USER_MODEL),
        ),
    ]
