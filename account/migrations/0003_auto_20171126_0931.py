# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_address_full_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderitem',
            options={'ordering': ('-created', '-updated', 'item_return', 'cashback')},
        ),
        migrations.AddField(
            model_name='orderitem',
            name='cashback',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='item_return',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
