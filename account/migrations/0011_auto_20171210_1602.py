# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20171210_1053'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('if_exchange', 'if_return', 'cashback', '-created', '-updated')},
        ),
        migrations.RenameField(
            model_name='order',
            old_name='item_return',
            new_name='if_return',
        ),
        migrations.AddField(
            model_name='order',
            name='exchange_item',
            field=models.ManyToManyField(related_name='items_exchanged', to='account.OrderItem', blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='exchanged',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='if_exchange',
            field=models.BooleanField(default=False),
        ),
    ]
