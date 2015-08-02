# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0014_auto_20150802_0154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engineeringambassador',
            name='student_id',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
    ]
