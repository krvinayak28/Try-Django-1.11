# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-02-22 17:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_auto_20190222_1653'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Restaurants',
            new_name='RestaurantLocation',
        ),
    ]
