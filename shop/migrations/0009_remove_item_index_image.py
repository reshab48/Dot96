# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20171121_0726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='index_image',
        ),
    ]
