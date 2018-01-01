# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_item_wished'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='gst',
            field=models.DecimalField(default=18, max_digits=4, decimal_places=2),
        ),
    ]
