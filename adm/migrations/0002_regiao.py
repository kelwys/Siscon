# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Regiao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('descricao', models.CharField(verbose_name='Descrição', max_length=45)),
            ],
            options={
                'verbose_name': 'Região',
                'verbose_name_plural': 'Regiões',
            },
        ),
    ]
