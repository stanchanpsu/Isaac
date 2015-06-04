# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EngineeringAmbassador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picture', models.ImageField(upload_to=b'')),
                ('grad_date', models.DateField()),
                ('fall_status', models.BooleanField()),
                ('spring_status', models.BooleanField()),
                ('student_id', models.PositiveIntegerField()),
                ('company_designation', models.CharField(max_length=20)),
                ('companies_worked', models.TextField()),
                ('major', models.CharField(max_length=20)),
                ('major_2', models.CharField(max_length=20)),
                ('minor', models.CharField(max_length=20)),
                ('minor_2', models.CharField(max_length=20)),
                ('schreyer_honors', models.BooleanField()),
                ('phone', models.CharField(max_length=10)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
