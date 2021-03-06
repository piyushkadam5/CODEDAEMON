# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-27 23:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_problem_s_rate'),
        ('Reverse', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reverse',
            name='Contest',
        ),
        migrations.RemoveField(
            model_name='reverse',
            name='p_cons',
        ),
        migrations.RemoveField(
            model_name='reverse',
            name='p_disc',
        ),
        migrations.RemoveField(
            model_name='reverse',
            name='p_input',
        ),
        migrations.RemoveField(
            model_name='reverse',
            name='p_level',
        ),
        migrations.RemoveField(
            model_name='reverse',
            name='p_name',
        ),
        migrations.RemoveField(
            model_name='reverse',
            name='p_output',
        ),
        migrations.RemoveField(
            model_name='reverse',
            name='s_rate',
        ),
        migrations.RemoveField(
            model_name='reverse',
            name='sample_input',
        ),
        migrations.RemoveField(
            model_name='reverse',
            name='sample_output',
        ),
        migrations.RemoveField(
            model_name='reverse',
            name='score',
        ),
        migrations.RemoveField(
            model_name='reverse',
            name='success_sub',
        ),
        migrations.RemoveField(
            model_name='reverse',
            name='tot_sub',
        ),
        migrations.AddField(
            model_name='reverse',
            name='Problem',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.Problem'),
            preserve_default=False,
        ),
    ]
