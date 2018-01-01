# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_address_default'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_total',
            field=models.PositiveIntegerField(),
        ),
    ]
