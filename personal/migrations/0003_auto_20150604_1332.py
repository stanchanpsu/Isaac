# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0002_auto_20150604_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engineeringambassador',
            name='picture',
            field=models.ImageField(upload_to=b'/profile_pics/', blank=True),
        ),
    ]
