from django.contrib import admin
from django import forms
from sen.models import *
from importcsvadmin.admin import ImportCSVModelAdmin

class DadosSensorAdminImporter(forms.ModelForm):
    class Meta:
        model = DadosSensores
        fields = ('tag', 'data_hora', 'valor')


class DadosSensoresAdmin(ImportCSVModelAdmin):
    importer_class = DadosSensorAdminImporter
    list_display = ['tag', 'data_hora', 'valor']


admin.site.register(TipoSensor)
admin.site.register(UnidadeMedida)
admin.site.register(Sensor)
admin.site.register(DadosSensores, DadosSensoresAdmin)