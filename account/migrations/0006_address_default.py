# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20171202_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='default',
            field=models.BooleanField(default=False),
        ),
    ]
