# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_item_index_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
