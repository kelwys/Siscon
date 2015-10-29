from django.db import models
from adm.models import Regiao, Municipio

class TipoSensor(models.Model):
    descricao = models.CharField(
        max_length=45, verbose_name='Descrição')

    class Meta:
        verbose_name = 'Tipo de Sensor'
        verbose_name_plural = 'Tipos de Sensores'

    def __str__(self):
        return self.descricao


class UnidadeMedida(models.Model):
    descricao = models.CharField(
        max_length=45, verbose_name='Unidade')

    class Meta:
        verbose_name = 'Unidade de Medida'
        verbose_name_plural = 'Unidades de Medida'

    def __str__(self):
        return self.descricao


class Sensor(models.Model):
    nome = models.CharField(max_length=45, verbose_name='Nome')
    tipo = model.models.ForeignKey(TipoSensor, verbose_name='Tipo de Sensor')
    regiao = models.ForeignKey(Regiao, verbose_name='Região')
    unidade = models.ForeignKey(UnidadeMedida, verbose_name='Unidade de Medida')
    faixa_valor = models.CharField(max_length=45, verbose_name='Faixa de Valores')
    municipio = models.ForeignKey(Municipio, verbose_name='Municipio')

    class Meta:
        verbose_name = 'Sensor'
        verbose_name_plural = 'Sensores'

    def __str__(self):
        return self.nome