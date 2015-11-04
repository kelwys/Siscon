# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DadosSensores',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('data_hora', models.DateTimeField(verbose_name='Data e hora')),
                ('valor', models.DecimalField(verbose_name='Valor', decimal_places=2, max_digits=6)),
                ('nome', models.ForeignKey(verbose_name='Nome', to='sen.Sensor')),
            ],
            options={
                'verbose_name': 'Dados do Sensor',
                'verbose_name_plural': 'Dados dos Sensores',
            },
        ),
    ]
