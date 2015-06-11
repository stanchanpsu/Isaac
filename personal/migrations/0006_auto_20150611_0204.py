# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0005_auto_20150604_1636'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='engineeringambassador',
            name='grad_date',
        ),
        migrations.AddField(
            model_name='engineeringambassador',
            name='grad_semester',
            field=models.CharField(max_length=6, blank=True),
        ),
        migrations.AddField(
            model_name='engineeringambassador',
            name='grad_year',
            field=models.CharField(max_length=4, blank=True),
        ),
    ]
