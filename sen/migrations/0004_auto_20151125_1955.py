# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('sen', '0003_auto_20151105_1918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensor',
            name='faixa_valor',
        ),
        migrations.AddField(
            model_name='sensor',
            name='valor_max',
            field=models.DecimalField(decimal_places=2, max_digits=6, default=0, verbose_name='Valor Maximo'),
        ),
        migrations.AddField(
            model_name='sensor',
            name='valor_min',
            field=models.DecimalField(decimal_places=2, max_digits=6, default=0, verbose_name='Valor Minimo'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='unidade',
            field=smart_selects.db_fields.ChainedForeignKey(to='sen.UnidadeMedida', verbose_name='Unidade de Medida'),
        ),
    ]
