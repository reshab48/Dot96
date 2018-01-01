# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('info', models.CharField(max_length=150)),
            ],
            options={
                'ordering': ('item',),
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('index_image', models.ImageField(upload_to=b'items/')),
                ('description', models.TextField(blank=True)),
                ('stock', models.PositiveIntegerField()),
                ('available', models.BooleanField(default=True)),
                ('price', models.DecimalField(max_digits=15, decimal_places=2)),
                ('retail_dis', models.DecimalField(max_digits=4, decimal_places=2)),
                ('wholesale_dis', models.DecimalField(max_digits=4, decimal_places=2)),
                ('popularity', models.PositiveIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-created', '-updated'),
            },
        ),
        migrations.CreateModel(
            name='ItemColour',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('colour', models.CharField(max_length=10)),
                ('hex_value', models.CharField(max_length=10, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('item', models.ForeignKey(related_name='item_colours', to='shop.Item')),
            ],
            options={
                'ordering': ('-created', '-updated'),
            },
        ),
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'items/images')),
                ('item_colour', models.ForeignKey(related_name='item_images', to='shop.ItemColour')),
            ],
        ),
        migrations.CreateModel(
            name='Promo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'promos/')),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('category', models.ForeignKey(related_name='sub_categories', to='shop.Category')),
            ],
        ),
        migrations.AddField(
            model_name='promo',
            name='sub_category',
            field=models.ForeignKey(related_name='promotions', to='shop.SubCategory'),
        ),
        migrations.AddField(
            model_name='item',
            name='sub_category',
            field=models.ForeignKey(related_name='items', to='shop.SubCategory'),
        ),
        migrations.AddField(
            model_name='detail',
            name='item',
            field=models.ForeignKey(related_name='details', to='shop.Item'),
        ),
        migrations.AlterIndexTogether(
            name='category',
            index_together=set([('id', 'slug')]),
        ),
    ]
