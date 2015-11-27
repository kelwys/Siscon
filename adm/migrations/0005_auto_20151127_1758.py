# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0004_auto_20151126_0155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bairro',
            name='municipio',
            field=models.ForeignKey(to='adm.Municipio', verbose_name='Município'),
        ),
    ]
