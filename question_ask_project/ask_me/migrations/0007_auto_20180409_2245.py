# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-09 19:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask_me', '0006_auto_20180409_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='upload',
            field=models.ImageField(default='src/default_avatar.png', upload_to='uploads/%Y/%m/%d/', verbose_name="User's Avatar"),
        ),
    ]
