# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-09 13:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='contact',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]