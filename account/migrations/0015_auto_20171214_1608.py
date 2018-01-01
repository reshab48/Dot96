# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_auto_20171214_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivered_on',
            field=models.DateTimeField(default=django.utils.timezone.now, blank=True),
        ),
    ]
