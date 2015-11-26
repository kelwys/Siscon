from django.contrib import admin
from adm.models import *



class EnderecoInline(admin.TabularInline):
    model = Endereco
    # form = ChoiceEnderecoFormset
    # classes = ('collapse open',)
    # inline_classes = ('collapse open',)
    extra = 0



class RegiaoAdmin(admin.ModelAdmin):
    # readonly_fields = ['identificador', ]
    fieldsets = [
        ('Dados Região', {'fields': [
            'descricao']})]


class PessoaAdmin(admin.ModelAdmin):
    # form = PessoaForm
    fieldsets = [
        ('Dados Pessoais', {'fields': [
            'nome', 'sexo', 'cpf',
			'observacoes']}),
        ('Login', {'fields': ['user']})]

    list_display = ['nome', 'cpf']
    search_fields = ['nome', 'cpf']
    # change_list_filter_template = "admin/filter_listing.html"

admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Bairro)
admin.site.register(Municipio)
admin.site.register(Estado)
admin.site.register(Pais)
admin.site.register(Endereco)
admin.site.register(Regiao, RegiaoAdmin)

# Register your models here.
