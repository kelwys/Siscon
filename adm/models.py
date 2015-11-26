from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from django.db.models import signals
from django.contrib.auth.models import User
from django.db.models import F, Sum, Max, FloatField, ExpressionWrapper

# from sen.models import Sensor
# Create your models here.

GENERO = (('0', 'Masculino'), ('1', 'Feminino'))


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


class Regiao(models.Model):
    descricao = models.CharField(
        max_length=45, verbose_name='Descrição')

    class Meta:
        verbose_name = 'Região'
        verbose_name_plural = 'Regiões'

    # def gerar_identificador_regiao(self):
    #     if self.identificador is None:
    #         self.identificador = 1
    #         if Regiao.objects.exists():
    #             self.identificador = Regiao.objects.all().aggregate(
    #                 Max('identificador')).get('identificador__max') + 1
    #
    # def save(self):
    #     self.gerar_identificador_regiao()
    #     super(Regiao, self).save()

    def __str__(self):
        return self.descricao


class Municipio(models.Model):
    estado = models.ForeignKey(Estado, verbose_name='Estado')
    regiao = models.ForeignKey(Regiao, verbose_name='Região')
    municipio = models.CharField(max_length=150, verbose_name='Município')

    class Meta:
        verbose_name = 'Município'
        verbose_name_plural = 'Municípios'

    def __str__(self):
        return self.municipio


class Bairro(models.Model):
    bairro = models.CharField(max_length=150, verbose_name='Bairro')
    municipio = ChainedForeignKey(
        Municipio, chained_field="estado",
        chained_model_field="estado",
        show_all=False, auto_choose=True, verbose_name='Município')

    class Meta:
        verbose_name = 'Bairro'
        verbose_name_plural = 'Bairros'

    def __str__(self):
        return self.bairro


class Endereco(models.Model):
    bairro = models.ForeignKey(Bairro, verbose_name='Bairro')
    logradouro = models.CharField(blank=True, null=True, max_length=150)
    cep = models.CharField(blank=True, null=True, max_length=10)

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

    def __str__(self):
        return str(self.tipo)


class Pessoa(models.Model):
    cpf = models.CharField(max_length=11, verbose_name='CPF')
    nome = models.CharField(max_length=200)
    sexo = models.IntegerField(choices=GENERO)
    observacoes = models.TextField(
        blank=True, null=True, verbose_name='Observações')
    user = models.OneToOneField(User, verbose_name='Usuário')
    endereco = models.ForeignKey(Endereco, verbose_name='Endereço')

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
