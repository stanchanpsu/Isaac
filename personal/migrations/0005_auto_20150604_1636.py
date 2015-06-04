# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0004_auto_20150604_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engineeringambassador',
            name='grad_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
