# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_auto_20150518_0250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outreachtrip',
            name='EAs_registered',
            field=models.ManyToManyField(related_name='outreach', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tour',
            name='tour_type',
            field=models.CharField(default=b'regular', max_length=3, choices=[(b'REG', b'Regular'), (b'ASP', b'ASP'), (b'VIP', b'VIP'), (b'OTR', b'Other')]),
        ),
    ]
