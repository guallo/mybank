# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-09 20:08
from __future__ import unicode_literals

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20160509_0433'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4()),
            preserve_default=False,
        ),
    ]