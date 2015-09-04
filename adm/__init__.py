from __future__ import absolute_import
from django.apps import AppConfig


class AdmConfig(AppConfig):
    name = 'adm'
    verbose_name = u"Administrativo"
    label= 'adm'

default_app_config = 'adm.AdmConfig'