# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-08 16:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('bills', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='priority',
            field=models.IntegerField(
                choices=[(1, 'High'), (2, 'Medium'), (3, 'Low')],
                max_length=200),
        ),
        migrations.AlterField(
            model_name='bill',
            name='status',
            field=models.IntegerField(
                choices=[(1, 'Needs Review'), (2, 'Updated'),
                         (3, 'Research Complete'), (4, 'Done')],
                max_length=200),
        ),
    ]
