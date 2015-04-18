# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20150417_2043'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='EAsneeded',
            new_name='EAs_needed',
        ),
    ]
