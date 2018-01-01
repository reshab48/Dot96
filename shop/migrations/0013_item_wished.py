# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0012_remove_itemcolour_sub_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='wished',
            field=models.ManyToManyField(related_name='items_liked', to=settings.AUTH_USER_MODEL),
        ),
    ]
