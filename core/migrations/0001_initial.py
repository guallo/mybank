# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-07 05:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Move',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typee', models.IntegerField(choices=[(1, 'DEPOSIT'), (2, 'EXTRACTION')])),
                ('description', models.CharField(max_length=256)),
            ],
        ),
    ]
