from django.db import models
from adm.models import Regiao, Municipio
from adaptor.model import CsvModel

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
    tipo = models.ForeignKey(TipoSensor, verbose_name='Tipo de Sensor')
    regiao = models.ForeignKey(Regiao, verbose_name='Região')
    unidade = models.ForeignKey(UnidadeMedida, verbose_name='Unidade de Medida')
    faixa_valor = models.CharField(max_length=45, verbose_name='Faixa de Valores')
    municipio = models.ForeignKey(Municipio, verbose_name='Municipio')

    class Meta:
        verbose_name = 'Sensor'
        verbose_name_plural = 'Sensores'

    def __str__(self):
        return self.nome

# class MyCSvModel(CsvModel):
#     nome = models.CharField()
#     data_hora = models.DateTimeField()
#     valor = models.DecimalField()

#     class Meta:
#         delimiter = ";"
#         dbModel = DadosSensores


class DadosSensores(models.Model):
    nome = models.ForeignKey(Sensor, verbose_name='Nome')
    data_hora = models.DateTimeField(verbose_name='Data e hora')
    valor = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Valor')

    class Meta:
        verbose_name = 'Dados do Sensor'
        verbose_name_plural = 'Dados dos Sensores'

    def __str__(self):
        return self.nome