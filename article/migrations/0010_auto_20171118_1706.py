# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-18 14:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0009_auto_20171118_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
