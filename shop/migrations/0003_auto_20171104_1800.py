# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_item_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='retail_price',
            field=models.DecimalField(default=0, max_digits=15, decimal_places=2),
        ),
        migrations.AddField(
            model_name='item',
            name='wholesale_price',
            field=models.DecimalField(default=0, max_digits=15, decimal_places=2),
        ),
    ]
