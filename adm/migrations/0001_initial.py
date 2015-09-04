# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bairro',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('bairro', models.CharField(verbose_name='Bairro', max_length=150)),
            ],
            options={
                'verbose_name': 'Bairro',
                'verbose_name_plural': 'Bairros',
            },
        ),
        migrations.CreateModel(
            name='EMail',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('email', models.EmailField(verbose_name='E-mail', max_length=60)),
                ('ativo', models.BooleanField()),
            ],
            options={
                'verbose_name': 'E-mail',
                'verbose_name_plural': 'E-mails',
            },
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('logradouro', models.CharField(null=True, max_length=150, blank=True)),
                ('cep', models.CharField(null=True, max_length=10, blank=True)),
                ('complemento', models.CharField(null=True, max_length=150, blank=True)),
                ('bairro', smart_selects.db_fields.ChainedForeignKey(chained_model_field='municipio', chained_field='municipio', verbose_name='Bairro', auto_choose=True, null=True, blank=True, to='adm.Bairro')),
            ],
            options={
                'verbose_name': 'Endereço',
                'verbose_name_plural': 'Endereços',
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('estado', models.CharField(verbose_name='Estado', max_length=45)),
                ('uf', models.CharField(verbose_name='UF', max_length=3)),
            ],
            options={
                'verbose_name': 'Estado',
                'verbose_name_plural': 'Estados',
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('municipio', models.CharField(verbose_name='Município', max_length=150)),
                ('estado', models.ForeignKey(verbose_name='Estado', to='adm.Estado')),
            ],
            options={
                'verbose_name': 'Município',
                'verbose_name_plural': 'Municípios',
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('pais', models.CharField(verbose_name='País', max_length=100)),
                ('sigla', models.CharField(verbose_name='Sigla', max_length=5)),
            ],
            options={
                'verbose_name': 'País',
                'verbose_name_plural': 'Países',
            },
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('cpf', models.CharField(verbose_name='CPF', max_length=11)),
                ('data_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('foto', models.ImageField(null=True, upload_to='', blank=True)),
                ('nome', models.CharField(max_length=200)),
                ('sexo', models.IntegerField()),
                ('identidade', models.CharField(verbose_name='Identidade', null=True, max_length=45, blank=True)),
                ('documento_profissional', models.CharField(verbose_name='Documento Profissional', null=True, max_length=45, blank=True)),
                ('nacionalidade', models.IntegerField()),
                ('observacoes', models.TextField(verbose_name='Observações', null=True, blank=True)),
                ('estado', smart_selects.db_fields.ChainedForeignKey(chained_model_field='pais', verbose_name='Estado de Nascimento', auto_choose=True, chained_field='pais', to='adm.Estado')),
                ('municipio', smart_selects.db_fields.ChainedForeignKey(chained_model_field='estado', verbose_name='Município de Nascimento', auto_choose=True, chained_field='estado', to='adm.Municipio')),
                ('pais', models.ForeignKey(verbose_name='País de Nascimento', to='adm.Pais')),
                ('user', models.OneToOneField(verbose_name='Usuário', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Pessoas',
            },
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('telefone', models.CharField(verbose_name='Telefone', max_length=20)),
                ('pessoa', models.ForeignKey(to='adm.Pessoa')),
            ],
            options={
                'verbose_name': 'Telefone',
                'verbose_name_plural': 'Telefones',
            },
        ),
        migrations.CreateModel(
            name='TipoTelefone',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('tipo_telefone', models.CharField(verbose_name='Tipo de Telefone', max_length=45)),
            ],
            options={
                'verbose_name': 'Tipo de Telefone',
                'verbose_name_plural': 'Tipos de Telefones',
            },
        ),
        migrations.AddField(
            model_name='telefone',
            name='tipo',
            field=models.ForeignKey(verbose_name='Tipo', to='adm.TipoTelefone'),
        ),
        migrations.AddField(
            model_name='estado',
            name='pais',
            field=models.ForeignKey(verbose_name='País', to='adm.Pais'),
        ),
        migrations.AddField(
            model_name='endereco',
            name='estado',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field='pais', verbose_name='Estado', show_all=True, auto_choose=True, chained_field='pais', to='adm.Estado'),
        ),
        migrations.AddField(
            model_name='endereco',
            name='municipio',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field='estado', verbose_name='Município', auto_choose=True, chained_field='estado', to='adm.Municipio'),
        ),
        migrations.AddField(
            model_name='endereco',
            name='pais',
            field=models.ForeignKey(verbose_name='País', to='adm.Pais'),
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
            field=models.ForeignKey(verbose_name='Estado', to='adm.Estado'),
        ),
        migrations.AddField(
            model_name='bairro',
            name='municipio',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field='estado', verbose_name='Município', auto_choose=True, chained_field='estado', to='adm.Municipio'),
        ),
    ]
