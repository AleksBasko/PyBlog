# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-15 10:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_testing'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Testing',
        ),
    ]