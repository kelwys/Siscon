# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sen', '0002_auto_20151105_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='tag',
            field=models.CharField(max_length=45, unique=True, primary_key=True, serialize=False),
        ),
    ]
