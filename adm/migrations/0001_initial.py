# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bairro',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('bairro', models.CharField(max_length=150, verbose_name='Bairro')),
            ],
            options={
                'verbose_name_plural': 'Bairros',
                'verbose_name': 'Bairro',
            },
        ),
        migrations.CreateModel(
            name='EMail',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('email', models.EmailField(max_length=60, verbose_name='E-mail')),
                ('ativo', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'E-mails',
                'verbose_name': 'E-mail',
            },
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('logradouro', models.CharField(blank=True, max_length=150, null=True)),
                ('cep', models.CharField(blank=True, max_length=10, null=True)),
                ('complemento', models.CharField(blank=True, max_length=150, null=True)),
                ('bairro', smart_selects.db_fields.ChainedForeignKey(blank=True, chained_field='municipio', to='adm.Bairro', auto_choose=True, chained_model_field='municipio', null=True, verbose_name='Bairro')),
            ],
            options={
                'verbose_name_plural': 'Endereços',
                'verbose_name': 'Endereço',
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('estado', models.CharField(max_length=45, verbose_name='Estado')),
                ('uf', models.CharField(max_length=3, verbose_name='UF')),
            ],
            options={
                'verbose_name_plural': 'Estados',
                'verbose_name': 'Estado',
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('municipio', models.CharField(max_length=150, verbose_name='Município')),
                ('estado', models.ForeignKey(to='adm.Estado', verbose_name='Estado')),
            ],
            options={
                'verbose_name_plural': 'Municípios',
                'verbose_name': 'Município',
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('pais', models.CharField(max_length=100, verbose_name='País')),
                ('sigla', models.CharField(max_length=5, verbose_name='Sigla')),
            ],
            options={
                'verbose_name_plural': 'Países',
                'verbose_name': 'País',
            },
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF')),
                ('data_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('nome', models.CharField(max_length=200)),
                ('sexo', models.IntegerField(choices=[('0', 'Masculino'), ('1', 'Feminino')])),
                ('identidade', models.CharField(blank=True, max_length=45, null=True, verbose_name='Identidade')),
                ('observacoes', models.TextField(blank=True, null=True, verbose_name='Observações')),
                ('estado', smart_selects.db_fields.ChainedForeignKey(chained_field='pais', to='adm.Estado', auto_choose=True, chained_model_field='pais', verbose_name='Estado de Nascimento')),
                ('municipio', smart_selects.db_fields.ChainedForeignKey(chained_field='estado', to='adm.Municipio', auto_choose=True, chained_model_field='estado', verbose_name='Município de Nascimento')),
                ('pais', models.ForeignKey(to='adm.Pais', verbose_name='País de Nascimento')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name_plural': 'Pessoas',
                'verbose_name': 'Pessoa',
            },
        ),
        migrations.CreateModel(
            name='Regiao',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('identificador', models.IntegerField(verbose_name='ID')),
                ('descricao', models.CharField(max_length=45, verbose_name='Descrição')),
            ],
            options={
                'verbose_name_plural': 'Regiões',
                'verbose_name': 'Região',
            },
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('telefone', models.CharField(max_length=20, verbose_name='Telefone')),
                ('pessoa', models.ForeignKey(to='adm.Pessoa')),
            ],
            options={
                'verbose_name_plural': 'Telefones',
                'verbose_name': 'Telefone',
            },
        ),
        migrations.CreateModel(
            name='TipoTelefone',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('tipo_telefone', models.CharField(max_length=45, verbose_name='Tipo de Telefone')),
            ],
            options={
                'verbose_name_plural': 'Tipos de Telefones',
                'verbose_name': 'Tipo de Telefone',
            },
        ),
        migrations.AddField(
            model_name='telefone',
            name='tipo',
            field=models.ForeignKey(to='adm.TipoTelefone', verbose_name='Tipo'),
        ),
        migrations.AddField(
            model_name='estado',
            name='pais',
            field=models.ForeignKey(to='adm.Pais', verbose_name='País'),
        ),
        migrations.AddField(
            model_name='endereco',
            name='estado',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='pais', to='adm.Estado', auto_choose=True, show_all=True, chained_model_field='pais', verbose_name='Estado'),
        ),
        migrations.AddField(
            model_name='endereco',
            name='municipio',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='estado', to='adm.Municipio', auto_choose=True, chained_model_field='estado', verbose_name='Município'),
        ),
        migrations.AddField(
            model_name='endereco',
            name='pais',
            field=models.ForeignKey(to='adm.Pais', verbose_name='País'),
        ),
        migrations.AddField(
            model_name='endereco',
            name='pessoa',
            field=models.ForeignKey(to='adm.Pessoa'),
        ),
        migrations.AddField(
            model_name='email',
            name='pessoa',
            field=models.ForeignKey(to='adm.Pessoa'),
        ),
        migrations.AddField(
            model_name='bairro',
            name='estado',
            field=models.ForeignKey(to='adm.Estado', verbose_name='Estado'),
        ),
        migrations.AddField(
            model_name='bairro',
            name='municipio',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='estado', to='adm.Municipio', auto_choose=True, chained_model_field='estado', verbose_name='Município'),
        ),
    ]
