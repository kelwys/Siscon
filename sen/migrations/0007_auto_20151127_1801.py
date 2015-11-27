# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sen', '0006_auto_20151126_0155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='unidade',
            field=models.ForeignKey(to='sen.UnidadeMedida', verbose_name='Unidade de Medida'),
        ),
    ]
