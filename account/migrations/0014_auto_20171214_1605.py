# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_auto_20171213_0803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivered_on',
            field=models.DateTimeField(blank=True),
        ),
    ]
