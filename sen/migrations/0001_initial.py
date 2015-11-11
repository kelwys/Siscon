# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0002_auto_20151029_1329'),
    ]

    operations = [
        migrations.CreateModel(
            name='DadosSensores',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('data_hora', models.DateTimeField(verbose_name='Data e hora')),
                ('valor', models.DecimalField(max_digits=6, verbose_name='Valor', decimal_places=2)),
            ],
            options={
                'verbose_name_plural': 'Dados dos Sensores',
                'verbose_name': 'Dados do Sensor',
            },
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('tag', models.CharField(serialize=False, unique=True, max_length=45, primary_key=True, default='TERM')),
                ('faixa_valor', models.CharField(verbose_name='Faixa de Valores', max_length=45)),
                ('municipio', models.ForeignKey(verbose_name='Municipio', to='adm.Municipio')),
            ],
            options={
                'verbose_name_plural': 'Sensores',
                'verbose_name': 'Sensor',
            },
        ),
        migrations.CreateModel(
            name='TipoSensor',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('descricao', models.CharField(verbose_name='Descrição', max_length=45)),
            ],
            options={
                'verbose_name_plural': 'Tipos de Sensores',
                'verbose_name': 'Tipo de Sensor',
            },
        ),
        migrations.CreateModel(
            name='UnidadeMedida',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('descricao', models.CharField(verbose_name='Unidade', max_length=45)),
                ('tipo', models.ForeignKey(verbose_name='Tipo de Sensor', to='sen.TipoSensor')),
            ],
            options={
                'verbose_name_plural': 'Unidades de Medida',
                'verbose_name': 'Unidade de Medida',
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
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field='tipo', verbose_name='Unidade de Medida', to='sen.UnidadeMedida', auto_choose=True, chained_field='tipo'),
        ),
        migrations.AddField(
            model_name='dadossensores',
            name='tag',
            field=models.ForeignKey(verbose_name='Tag', default='01', to='sen.Sensor'),
        ),
    ]
