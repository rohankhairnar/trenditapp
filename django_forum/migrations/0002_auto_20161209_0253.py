# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-09 02:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
    ]
