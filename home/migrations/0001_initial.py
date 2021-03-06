# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-08 15:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('con_name', models.CharField(max_length=250)),
                ('con_date', models.DateField(blank=True)),
                ('start_time', models.TimeField(blank=True)),
                ('end_time', models.TimeField(blank=True)),
                ('org_name', models.CharField(max_length=250)),
                ('image', models.CharField(max_length=250)),
                ('tagline', models.CharField(max_length=250)),
                ('desc', models.CharField(max_length=250)),
                ('rules', models.CharField(max_length=250)),
                ('prize', models.CharField(max_length=250)),
                ('scoring', models.CharField(max_length=250)),
            ],
        ),
    ]
