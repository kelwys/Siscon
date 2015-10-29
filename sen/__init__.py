from __future__ import absolute_import
from django.apps import AppConfig


class senConfig(AppConfig):
    name = 'sen'
    verbose_name = u"Sensores"
    label= 'sen'

default_app_config = 'sen.senConfig'