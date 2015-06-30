# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groupme', '0003_auto_20150627_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='image_url',
            field=models.CharField(default=None, max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=40, blank=True),
        ),
    ]
