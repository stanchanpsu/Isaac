# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_auto_20150515_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='tour_type',
            field=models.CharField(default=b'reg', max_length=3, choices=[(b'REG', b'Regular'), (b'ASP', b'ASP'), (b'VIP', b'VIP'), (b'OTH', b'Other')]),
        ),
    ]
