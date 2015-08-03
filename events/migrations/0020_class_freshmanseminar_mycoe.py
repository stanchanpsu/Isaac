# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0019_auto_20150521_1754'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('event_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='events.Event')),
                ('veterans', models.BooleanField(default=False)),
            ],
            bases=('events.event',),
        ),
        migrations.CreateModel(
            name='FreshmanSeminar',
            fields=[
                ('event_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='events.Event')),
                ('major', models.CharField(max_length=40)),
                ('professor', models.CharField(max_length=40)),
            ],
            bases=('events.event',),
        ),
        migrations.CreateModel(
            name='MyCoe',
            fields=[
                ('event_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='events.Event')),
            ],
            bases=('events.event',),
        ),
    ]
