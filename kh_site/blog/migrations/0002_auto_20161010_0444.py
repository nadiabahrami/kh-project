# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-10 04:44
from __future__ import unicode_literals

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='blog_photo',
            field=models.ImageField(blank=True, upload_to=blog.models._image_path),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(max_length=5000),
        ),
    ]