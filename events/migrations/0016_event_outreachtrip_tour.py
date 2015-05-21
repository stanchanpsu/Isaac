# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0015_auto_20150521_1505'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.TimeField()),
                ('date', models.DateField()),
                ('hours', models.DecimalField(max_digits=3, decimal_places=1)),
                ('location', models.CharField(max_length=140)),
                ('EAs_needed', models.PositiveSmallIntegerField()),
                ('note', models.CharField(max_length=500, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='OutreachTrip',
            fields=[
                ('event_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='events.Event')),
                ('school', models.CharField(max_length=30)),
                ('EAs_registered', models.ManyToManyField(related_name='outreach', to=settings.AUTH_USER_MODEL)),
            ],
            bases=('events.event',),
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('event_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='events.Event')),
                ('tour_type', models.CharField(default=b'regular', max_length=3, choices=[(b'REG', b'Regular'), (b'ASP', b'ASP'), (b'VIP', b'VIP'), (b'OTR', b'Other')])),
                ('EAs_registered', models.ManyToManyField(related_name='tours', to=settings.AUTH_USER_MODEL)),
            ],
            bases=('events.event',),
        ),
    ]
