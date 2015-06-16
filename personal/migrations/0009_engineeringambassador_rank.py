# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0008_auto_20150613_0711'),
    ]

    operations = [
        migrations.AddField(
            model_name='engineeringambassador',
            name='rank',
            field=models.CharField(default=b'Ambassador', max_length=20, blank=True),
        ),
    ]
