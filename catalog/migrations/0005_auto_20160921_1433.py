# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-21 04:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20160921_1422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='name',
        ),
        migrations.AddField(
            model_name='author',
            name='name',
            field=models.CharField(default='sahil', max_length=100),
            preserve_default=False,
        ),
      
       
    ]
