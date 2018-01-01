# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20171104_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=models.SlugField(unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='slug',
            field=models.SlugField(unique=True, max_length=100),
        ),
        migrations.AlterIndexTogether(
            name='subcategory',
            index_together=set([('id', 'slug')]),
        ),
    ]
