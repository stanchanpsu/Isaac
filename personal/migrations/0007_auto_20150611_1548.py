# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0006_auto_20150611_0204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engineeringambassador',
            name='grad_semester',
            field=models.CharField(default=b'Spring', max_length=6, blank=True),
        ),
        migrations.AlterField(
            model_name='engineeringambassador',
            name='grad_year',
            field=models.CharField(default=b'2015', max_length=4, blank=True),
        ),
    ]
