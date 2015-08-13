# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groupme', '0005_auto_20150630_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='image_url',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
        ),
    ]
