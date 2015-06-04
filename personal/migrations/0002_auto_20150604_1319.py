# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engineeringambassador',
            name='companies_worked',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='engineeringambassador',
            name='company_designation',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='engineeringambassador',
            name='grad_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='engineeringambassador',
            name='major_2',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='engineeringambassador',
            name='minor',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='engineeringambassador',
            name='minor_2',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='engineeringambassador',
            name='picture',
            field=models.ImageField(upload_to=b'', blank=True),
        ),
    ]
