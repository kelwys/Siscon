# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='pessoa',
        ),
        migrations.RemoveField(
            model_name='telefone',
            name='pessoa',
        ),
        migrations.RemoveField(
            model_name='telefone',
            name='tipo',
        ),
        migrations.RemoveField(
            model_name='endereco',
            name='complemento',
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='data_nascimento',
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='identidade',
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='municipio',
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='pais',
        ),
        migrations.AlterField(
            model_name='endereco',
            name='pessoa',
            field=models.ForeignKey(to='adm.Pessoa', null=True, blank=True),
        ),
        migrations.DeleteModel(
            name='EMail',
        ),
        migrations.DeleteModel(
            name='Telefone',
        ),
        migrations.DeleteModel(
            name='TipoTelefone',
        ),
    ]
