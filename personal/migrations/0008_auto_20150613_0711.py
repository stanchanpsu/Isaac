# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0007_auto_20150611_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engineeringambassador',
            name='major',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='engineeringambassador',
            name='major_2',
            field=models.CharField(max_length=40, blank=True),
        ),
        migrations.AlterField(
            model_name='engineeringambassador',
            name='minor',
            field=models.CharField(max_length=40, blank=True),
        ),
        migrations.AlterField(
            model_name='engineeringambassador',
            name='minor_2',
            field=models.CharField(max_length=40, blank=True),
        ),
    ]
