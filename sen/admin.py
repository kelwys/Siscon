from django.contrib import admin
from django import forms
from sen.models import *
from importcsvadmin.admin import ImportCSVModelAdmin
from input_mask.fields import DecimalField
from django_csv_exports.admin import CSVExportAdmin


class DadosSensorAdminImporter(forms.ModelForm):
    data_hora = forms.DateField(widget=forms.DateInput(format = '%Y%m%d %H:%M'),
                                 input_formats=('%Y%m%d %H:%M',))
    valor = DecimalField(max_digits=6, decimal_places=2, localize=True)

    class Meta:
        model = DadosSensores
        fields = ('tag', 'data_hora', 'valor')


class DadosSensoresAdmin(ImportCSVModelAdmin, CSVExportAdmin):
    importer_class = DadosSensorAdminImporter
    list_filter = ['tag', 'tag__municipio', 'data_hora']
    list_display = ['tag', 'tag__municipio', 'data_hora', 'valor']
    csv_fields = ['tag', 'data_hora', 'valor']

    def tag__municipio(self, obj):
        return obj.tag.municipio.municipio
    tag__municipio.short_description = u'Municipio'



admin.site.register(TipoSensor)
admin.site.register(UnidadeMedida)
admin.site.register(Sensor)
admin.site.register(DadosSensores, DadosSensoresAdmin)