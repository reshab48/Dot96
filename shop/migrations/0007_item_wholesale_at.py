# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20171108_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='wholesale_at',
            field=models.PositiveIntegerField(default=3),
        ),
    ]
