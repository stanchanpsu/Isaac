# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0012_auto_20150627_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engineeringambassador',
            name='fall_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='engineeringambassador',
            name='major',
            field=models.CharField(max_length=40, blank=True),
        ),
        migrations.AlterField(
            model_name='engineeringambassador',
            name='phone',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='engineeringambassador',
            name='spring_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='engineeringambassador',
            name='student_id',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]
