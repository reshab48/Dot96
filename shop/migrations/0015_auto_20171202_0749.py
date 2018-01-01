# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_subcategory_gst'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='retail_dis',
            field=models.DecimalField(max_digits=4, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='wholesale_dis',
            field=models.DecimalField(max_digits=4, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='wished',
            field=models.ManyToManyField(related_name='items_liked', to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
