# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0022_auto_20150810_1608'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Class',
            new_name='ENGRClass',
        ),
        migrations.AlterModelOptions(
            name='engrclass',
            options={'verbose_name_plural': 'ENGR classes'},
        ),
        migrations.AlterField(
            model_name='event',
            name='EAs_registered',
            field=models.ManyToManyField(related_name='event', to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
