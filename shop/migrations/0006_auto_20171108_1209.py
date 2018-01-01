# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20171108_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemcolour',
            name='sub_category',
            field=models.ForeignKey(default=1, to='shop.SubCategory'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='sub_category',
            field=models.ForeignKey(to='shop.SubCategory'),
        ),
        migrations.AlterField(
            model_name='itemcolour',
            name='colour_image',
            field=models.ImageField(upload_to=b'colours/'),
        ),
        migrations.AlterField(
            model_name='itemcolour',
            name='item',
            field=models.ForeignKey(to='shop.Item'),
        ),
    ]
