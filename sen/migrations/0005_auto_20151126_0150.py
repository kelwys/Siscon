# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0003_auto_20151126_0150'),
        ('sen', '0004_auto_20151125_1955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unidademedida',
            name='tipo',
        ),
        migrations.AddField(
            model_name='sensor',
            name='endereco',
            field=models.ForeignKey(default=1, to='adm.Endereco', verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='valor_max',
            field=models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Valor Maximo'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='valor_min',
            field=models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Valor Minimo'),
        ),
    ]
