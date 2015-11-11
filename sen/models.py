from django.db import models
from adm.models import Regiao, Municipio
from datetime import datetime
from smart_selects.db_fields import ChainedForeignKey

class TipoSensor(models.Model):
    descricao = models.CharField(
        max_length=45, verbose_name='Descrição')

    class Meta:
        verbose_name = 'Tipo de Sensor'
        verbose_name_plural = 'Tipos de Sensores'

    def __str__(self):
        return self.descricao

# TODO: Colocar forengkey de tipo de sensor no model UnidadeMedida. Configurar smartselect
class UnidadeMedida(models.Model):
    tipo = models.ForeignKey(TipoSensor, verbose_name='Tipo de Sensor')
    descricao = models.CharField(max_length=45, verbose_name='Unidade')

    class Meta:
        verbose_name = 'Unidade de Medida'
        verbose_name_plural = 'Unidades de Medida'

    def __str__(self):
        return self.descricao


class Sensor(models.Model):
    tag = models.CharField(primary_key=True, unique=True, max_length=45)
    tipo = models.ForeignKey(TipoSensor, verbose_name='Tipo de Sensor')
    unidade = ChainedForeignKey(UnidadeMedida, "tipo")
    # unidade = ChainedForeignKey(UnidadeMedida, chained_field="tipo",
    #     chained_model_field="tipo", show_all=False,
    #     auto_choose=True, verbose_name='Unidade de Medida')
    faixa_valor = models.CharField(max_length=45, verbose_name='Faixa de Valores')
    municipio = models.ForeignKey(Municipio, verbose_name='Municipio')

    class Meta:
        verbose_name = 'Sensor'
        verbose_name_plural = 'Sensores'

    def __str__(self):
        return self.tag


# TODO: Configurar campos readonly no modo de edição
class DadosSensores(models.Model):
    tag = models.ForeignKey(Sensor, default='01', verbose_name='Tag')
    data_hora = models.DateTimeField(verbose_name='Data e hora')
    valor = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Valor')

    class Meta:
        verbose_name = 'Dados do Sensor'
        verbose_name_plural = 'Dados dos Sensores'

    def __str__(self):
        return self.tag.tag


