# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-21 05:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20160921_1444'),
    ]

    operations = [
        
        migrations.RemoveField(
            model_name='box',
            name='imprint',
        ),
        migrations.AlterField(
            model_name='author',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='box',
            name='box',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Book'),
        ),
    ]
