# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0002_auto_20151029_1329'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nome', models.CharField(verbose_name='Nome', max_length=45)),
                ('faixa_valor', models.CharField(verbose_name='Faixa de Valores', max_length=45)),
                ('municipio', models.ForeignKey(verbose_name='Municipio', to='adm.Municipio')),
                ('regiao', models.ForeignKey(verbose_name='Região', to='adm.Regiao')),
            ],
            options={
                'verbose_name': 'Sensor',
                'verbose_name_plural': 'Sensores',
            },
        ),
        migrations.CreateModel(
            name='TipoSensor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('descricao', models.CharField(verbose_name='Descrição', max_length=45)),
            ],
            options={
                'verbose_name': 'Tipo de Sensor',
                'verbose_name_plural': 'Tipos de Sensores',
            },
        ),
        migrations.CreateModel(
            name='UnidadeMedida',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('descricao', models.CharField(verbose_name='Unidade', max_length=45)),
            ],
            options={
                'verbose_name': 'Unidade de Medida',
                'verbose_name_plural': 'Unidades de Medida',
            },
        ),
        migrations.AddField(
            model_name='sensor',
            name='tipo',
            field=models.ForeignKey(verbose_name='Tipo de Sensor', to='sen.TipoSensor'),
        ),
        migrations.AddField(
            model_name='sensor',
            name='unidade',
            field=models.ForeignKey(verbose_name='Unidade de Medida', to='sen.UnidadeMedida'),
        ),
    ]
