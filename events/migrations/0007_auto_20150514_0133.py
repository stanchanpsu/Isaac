# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20150514_0131'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Outreach',
            new_name='Outreach_Trip',
        ),
    ]
