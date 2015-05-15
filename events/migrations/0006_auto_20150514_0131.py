# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20150417_2044'),
    ]

    operations = [
        migrations.CreateModel(
            name='Outreach',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('school', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('hours', models.DecimalField(max_digits=3, decimal_places=1)),
                ('location', models.CharField(max_length=140)),
                ('EAs_needed', models.PositiveSmallIntegerField()),
                ('note', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tour_type', models.CharField(default=b'reg', max_length=3, choices=[(b'REG', b'regular'), (b'ASP', b'accepted students day'), (b'VIP', b'very important person'), (b'OTH', b'other')])),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('hours', models.DecimalField(max_digits=3, decimal_places=1)),
                ('location', models.CharField(max_length=30)),
                ('EAs_needed', models.PositiveSmallIntegerField()),
                ('note', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='Event',
        ),
    ]
