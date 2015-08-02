# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0013_auto_20150802_0153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engineeringambassador',
            name='schreyer_honors',
            field=models.BooleanField(default=False),
        ),
    ]
