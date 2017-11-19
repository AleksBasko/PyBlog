# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-18 21:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0013_auto_20171118_2314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='like',
        ),
        migrations.AlterField(
            model_name='likearticle',
            name='like_article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Article'),
        ),
    ]