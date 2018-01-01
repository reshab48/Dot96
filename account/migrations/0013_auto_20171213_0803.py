# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_auto_20171213_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivered_on',
            field=models.DateTimeField(default=datetime.datetime.now, blank=True),
        ),
    ]
