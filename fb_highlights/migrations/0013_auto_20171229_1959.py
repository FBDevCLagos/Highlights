# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-12-29 19:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fb_highlights', '0012_auto_20171229_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='latesthighlight',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]
