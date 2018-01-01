# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_item_wholesale_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='available',
        ),
        migrations.RemoveField(
            model_name='item',
            name='stock',
        ),
        migrations.AddField(
            model_name='itemcolour',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='itemcolour',
            name='stock',
            field=models.PositiveIntegerField(default=30),
        ),
    ]
