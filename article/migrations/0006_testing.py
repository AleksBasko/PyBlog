# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-15 10:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20171113_2308'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments_text', models.TextField()),
                ('comments_article', models.IntegerField()),
            ],
            options={
                'db_table': 'testing',
            },
        ),
    ]
