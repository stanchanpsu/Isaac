# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20150514_0133'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Outreach_Trip',
            new_name='OutreachTrip',
        ),
    ]
