# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sen', '0007_auto_20151127_1801'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensor',
            name='endereco',
        ),
    ]
