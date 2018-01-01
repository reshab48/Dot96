# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_auto_20171202_0749'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0003_auto_20171126_0931'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('token', models.CharField(unique=True, max_length=10)),
                ('quantity', models.PositiveIntegerField()),
                ('paid', models.BooleanField(default=False)),
                ('item_return', models.BooleanField(default=False)),
                ('cashback', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('drop_out', models.ForeignKey(to='account.Address')),
                ('order_item', models.ManyToManyField(to='shop.ItemColour')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('item_return', 'cashback', '-created', '-updated'),
            },
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='colour',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='drop_out',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='item',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='user',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
