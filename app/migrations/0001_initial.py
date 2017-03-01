# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=35)),
                ('surname', models.CharField(max_length=35)),
                ('main', models.BooleanField(default=False)),
                ('about', models.TextField(default='Info about author')),
                ('image', models.ImageField(upload_to='img')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.TextField(unique=True, max_length=50)),
                ('image', models.ImageField(upload_to='img')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('company', models.TextField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.TextField(unique=True)),
                ('summary', models.TextField(default='summary')),
                ('text', models.TextField()),
                ('minute_read', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(to='app.Author')),
                ('category', models.ForeignKey(to='app.Category')),
            ],
        ),
    ]
