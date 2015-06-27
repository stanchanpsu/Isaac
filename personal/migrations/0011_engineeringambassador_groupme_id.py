# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0010_engineeringambassador_aboutme'),
    ]

    operations = [
        migrations.AddField(
            model_name='engineeringambassador',
            name='groupme_id',
            field=models.PositiveIntegerField(default=0, blank=True),
        ),
    ]
