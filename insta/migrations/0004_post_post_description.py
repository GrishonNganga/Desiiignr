# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-14 08:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0003_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_description',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
