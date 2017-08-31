# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 13:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobinfo',
            name='published',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='jobinfo',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 31, 13, 1, 45, 798946, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='jobinfo',
            name='department',
            field=models.CharField(default='Default', max_length=50),
        ),
        migrations.AlterField(
            model_name='jobinfo',
            name='job_position',
            field=models.CharField(default='Employee', max_length=50),
        ),
        migrations.AlterField(
            model_name='jobinfo',
            name='times_viewed',
            field=models.IntegerField(default=0),
        ),
    ]
