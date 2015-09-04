from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from django.db.models import signals
from django.contrib.auth.models import User
# Create your models here.

class Pais(models.Model):
    pais = models.CharField(max_length=100, verbose_name='País')
    sigla = models.CharField(max_length=5, verbose_name='Sigla')

    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Países'

    def __str__(self):
        return self.sigla


class Estado(models.Model):
    pais = models.ForeignKey(Pais, verbose_name='País')
    estado = models.CharField(max_length=45, verbose_name='Estado')
    uf = models.CharField(max_length=3, verbose_name='UF')

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'

    def __str__(self):
        return self.estado


class Municipio(models.Model):
    estado = models.ForeignKey(Estado, verbose_name='Estado')
    municipio = models.CharField(max_length=150, verbose_name='Município')

    class Meta:
        verbose_name = 'Município'
        verbose_name_plural = 'Municípios'

    def __str__(self):
        return self.municipio


class Bairro(models.Model):
    bairro = models.CharField(max_length=150, verbose_name='Bairro')
    estado = models.ForeignKey(Estado, verbose_name='Estado')
    municipio = ChainedForeignKey(
        Municipio, chained_field="estado",
        chained_model_field="estado",
        show_all=False, auto_choose=True, verbose_name='Município')

    class Meta:
        verbose_name = 'Bairro'
        verbose_name_plural = 'Bairros'

    def __str__(self):
        return self.bairro


class Regiao(models.Model):
    descricao = models.CharField(
        max_length=45, verbose_name='Descrição')

    class Meta:
        verbose_name = 'Região'
        verbose_name_plural = 'Regiões'

    def __str__(self):
        return self.descricao


class Pessoa(models.Model):
    cpf = models.CharField(max_length=11, verbose_name='CPF')
    data_nascimento = models.DateField(verbose_name='Data de Nascimento')
    foto = models.ImageField(blank=True, null=True)
    nome = models.CharField(max_length=200)
    sexo = models.IntegerField()
    identidade = models.CharField(
        max_length=45, blank=True, null=True, verbose_name='Identidade')
    documento_profissional = models.CharField(
        max_length=45, blank=True, null=True,
        verbose_name='Documento Profissional')
    nacionalidade = models.IntegerField()
    pais = models.ForeignKey(Pais, verbose_name='País de Nascimento')
    estado = ChainedForeignKey(Estado,
                               chained_field="pais",
                               chained_model_field="pais",
                               show_all=False,
                               auto_choose=True,
                               verbose_name='Estado de Nascimento')
    municipio = ChainedForeignKey(Municipio,
                                  chained_field="estado",
                                  chained_model_field="estado",
                                  show_all=False,
                                  auto_choose=True,
                                  verbose_name='Município de Nascimento')
    observacoes = models.TextField(
        blank=True, null=True, verbose_name='Observações')
    user = models.OneToOneField(User, verbose_name='Usuário')

    @staticmethod
    def beforeinsert(sender, instance, **kwargs):
        pass

    @staticmethod
    def afterinsert(sender, instance, **kwargs):
        pass

    @staticmethod
    def beforedelete(sender, instance, **kwargs):
        pass

    @staticmethod
    def afterdelete(sender, instance, **kwargs):
        pass

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'

    def __str__(self):
        return self.nome + ' - ' + self.cpf


signals.pre_save.connect(Pessoa.beforeinsert, sender=Pessoa)
signals.post_save.connect(Pessoa.afterinsert, sender=Pessoa)
signals.pre_delete.connect(Pessoa.beforedelete, sender=Pessoa)
signals.post_delete.connect(Pessoa.afterdelete, sender=Pessoa)


class EMail(models.Model):
    pessoa = models.ForeignKey(Pessoa)
    email = models.EmailField(max_length=60, verbose_name='E-mail')
    ativo = models.BooleanField()

    class Meta:
        verbose_name = 'E-mail'
        verbose_name_plural = 'E-mails'

class Endereco(models.Model):
    pessoa = models.ForeignKey(Pessoa)
    pais = models.ForeignKey(Pais, verbose_name='País')
    estado = ChainedForeignKey(Estado,
                               chained_field="pais",
                               chained_model_field="pais",
                               show_all=True,
                               auto_choose=True,
                               verbose_name='Estado')
    municipio = ChainedForeignKey(Municipio,
                                  chained_field="estado",
                                  chained_model_field="estado",
                                  show_all=False,
                                  auto_choose=True,
                                  verbose_name='Município')
    bairro = ChainedForeignKey(Bairro, chained_field="municipio",
                               chained_model_field="municipio",
                               show_all=False,
                               auto_choose=True,
                               blank=True, null=True,
                               verbose_name='Bairro')
    logradouro = models.CharField(blank=True, null=True, max_length=150)
    cep = models.CharField(blank=True, null=True, max_length=10)
    complemento = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

    def __str__(self):
        return str(self.tipo)


class TipoTelefone(models.Model):
    tipo_telefone = models.CharField(
        max_length=45, verbose_name='Tipo de Telefone')

    class Meta:
        verbose_name = 'Tipo de Telefone'
        verbose_name_plural = 'Tipos de Telefones'

    def __str__(self):
        return self.tipo_telefone


class Telefone(models.Model):
    pessoa = models.ForeignKey(Pessoa)
    tipo = models.ForeignKey(TipoTelefone, verbose_name='Tipo')
    telefone = models.CharField(max_length=20, verbose_name='Telefone')

    class Meta:
        verbose_name = 'Telefone'
        verbose_name_plural = 'Telefones'
