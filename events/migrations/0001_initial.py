# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('hours', models.PositiveSmallIntegerField()),
                ('location', models.CharField(max_length=140)),
                ('EAsneeded', models.PositiveSmallIntegerField()),
                ('description', models.CharField(max_length=500)),
            ],
        ),
    ]
