# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('sen', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='unidade',
            field=smart_selects.db_fields.ChainedForeignKey(to='sen.UnidadeMedida', chained_field='tipo'),
        ),
    ]
