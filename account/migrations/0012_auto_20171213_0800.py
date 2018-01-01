# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_auto_20171210_1602'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('if_exchange', 'if_return', '-created', '-updated')},
        ),
        migrations.AddField(
            model_name='order',
            name='delivered_on',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 13, 7, 59, 55, 621416, tzinfo=utc), blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderitem',
            name='amount',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
