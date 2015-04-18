# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20150417_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='hours',
            field=models.DecimalField(max_digits=4, decimal_places=2),
        ),
    ]
