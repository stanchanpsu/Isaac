# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0011_engineeringambassador_groupme_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engineeringambassador',
            name='groupme_id',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
