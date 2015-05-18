# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_auto_20150518_0249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='EAs_registered',
            field=models.ManyToManyField(related_name='tours', to=settings.AUTH_USER_MODEL),
        ),
    ]
