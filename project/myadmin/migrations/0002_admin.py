# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-19 20:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminname', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=80)),
                ('addtime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
