# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0003_auto_20151126_0150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='bairro',
            field=models.ForeignKey(to='adm.Bairro', verbose_name='Bairro'),
        ),
        migrations.AlterField(
            model_name='municipio',
            name='regiao',
            field=models.ForeignKey(to='adm.Regiao', verbose_name='Região'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='endereco',
            field=models.ForeignKey(to='adm.Endereco', verbose_name='Endereço'),
        ),
    ]
