from django.contrib import admin
from django import forms
from sen.models import *
from importcsvadmin.admin import ImportCSVModelAdmin
from input_mask.fields import DecimalField
from django_csv_exports.admin import CSVExportAdmin
from admin_highcharts.admin import HighchartsModelAdmin


class DadosSensorAdminImporter(forms.ModelForm):
    data_hora = forms.DateField(widget=forms.DateInput(format='%Y%m%d %H:%M'),
                                input_formats=('%Y%m%d %H:%M',))
    valor = DecimalField(max_digits=6, decimal_places=2, localize=True)

    class Meta:
        model = DadosSensores
        fields = ('tag', 'data_hora', 'valor')


class DadosSensoresAdmin(HighchartsModelAdmin, CSVExportAdmin):
    importer_class = DadosSensorAdminImporter
    list_filter = ['tag', 'tag__municipio', 'data_hora']
    list_display = ['tag', 'tag__municipio', 'data_hora', 'valor']
    csv_fields = ['tag', 'data_hora', 'valor']
    readonly_fields = list_display
    # chart_type = 'spline'
    chart_category_name = 'data_hora'
    chart_serial_names = ('valor',)

    def tag__municipio(self, obj):
        return obj.tag.municipio.municipio
    tag__municipio.short_description = u'Municipio'

    def has_delete_permission(self, request, obj=None):
        return False


class SensorAdmin(admin.ModelAdmin):
    list_display = ('tag', 'municipio', 'tipo', 'unidade', 'valor_min', 'valor_max')

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(TipoSensor)
admin.site.register(UnidadeMedida)
admin.site.register(Sensor, SensorAdmin)
admin.site.register(DadosSensores, DadosSensoresAdmin)
