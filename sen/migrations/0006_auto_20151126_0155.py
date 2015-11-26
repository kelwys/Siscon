# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sen', '0005_auto_20151126_0150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='endereco',
            field=models.ForeignKey(to='adm.Endereco', verbose_name='Endereço'),
        ),
    ]
