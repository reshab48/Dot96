# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_auto_20171202_0749'),
        ('account', '0004_auto_20171202_1625'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.PositiveIntegerField()),
                ('item', models.ForeignKey(to='shop.ItemColour')),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
        migrations.AddField(
            model_name='order',
            name='order_total',
            field=models.DecimalField(default=0, max_digits=10000000, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='order_item',
            field=models.ManyToManyField(related_name='items_ordered', to='account.OrderItem'),
        ),
        migrations.AddField(
            model_name='order',
            name='return_item',
            field=models.ManyToManyField(related_name='items_returned', to='account.OrderItem', blank=True),
        ),
    ]
