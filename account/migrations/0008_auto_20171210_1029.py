# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20171203_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='token',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
