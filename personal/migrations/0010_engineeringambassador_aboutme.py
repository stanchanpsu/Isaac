# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0009_engineeringambassador_rank'),
    ]

    operations = [
        migrations.AddField(
            model_name='engineeringambassador',
            name='aboutme',
            field=models.TextField(max_length=500, blank=True),
        ),
    ]
