# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20171107_1522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemcolour',
            name='colour',
        ),
        migrations.RemoveField(
            model_name='itemcolour',
            name='hex_value',
        ),
        migrations.AddField(
            model_name='itemcolour',
            name='colour_image',
            field=models.ImageField(upload_to=b'colours/', blank=True),
        ),
    ]
