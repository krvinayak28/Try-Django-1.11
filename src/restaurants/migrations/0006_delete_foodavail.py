# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-02-22 17:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0005_foodavail'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FoodAvail',
        ),
    ]
