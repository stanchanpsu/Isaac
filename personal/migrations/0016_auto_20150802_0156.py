# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0015_auto_20150802_0155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engineeringambassador',
            name='groupme_id',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
