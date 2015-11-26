# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0002_auto_20151029_1329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bairro',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='endereco',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='endereco',
            name='municipio',
        ),
        migrations.RemoveField(
            model_name='endereco',
            name='pais',
        ),
        migrations.RemoveField(
            model_name='endereco',
            name='pessoa',
        ),
        migrations.RemoveField(
            model_name='regiao',
            name='identificador',
        ),
        migrations.AddField(
            model_name='municipio',
            name='regiao',
            field=models.ForeignKey(default=1, verbose_name='Região', to='adm.Regiao'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='endereco',
            field=models.ForeignKey(default=1, verbose_name='Endereço', to='adm.Endereco'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='bairro',
            field=models.ForeignKey(default=1, verbose_name='Bairro', to='adm.Bairro'),
        ),
    ]
