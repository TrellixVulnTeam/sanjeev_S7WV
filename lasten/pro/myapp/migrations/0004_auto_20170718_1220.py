# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-18 06:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20170718_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='CreateDate',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='ModifiedDate',
            field=models.DateField(auto_now=True),
        ),
    ]