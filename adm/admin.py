from django.contrib import admin
from adm.models import *


class EMailInline(admin.TabularInline):
    model = EMail
    extra = 0


class EnderecoInline(admin.StackedInline):
    model = Endereco
    # form = ChoiceEnderecoFormset
    classes = ('collapse open',)
    inline_classes = ('collapse open',)
    extra = 0


class TelefoneInline(admin.TabularInline):
    model = Telefone
    # form = ChoiceTelefoneFormset
    extra = 0


class PessoaAdmin(admin.ModelAdmin):
    # form = PessoaForm
    fieldsets = [
        ('Dados Pessoais', {'fields': [
        	'foto', 'nome', 'sexo', 'cpf',
			'data_nascimento', 'identidade',
			'documento_profissional', 'nacionalidade',
			'pais', 'estado', 'municipio', 'observacoes']}),
        ('Login', {'fields': ['user']})]
    inlines = [
        TelefoneInline, EnderecoInline, EMailInline]

    list_display = ['nome', 'cpf', 'data_nascimento']
    search_fields = ['nome', 'cpf', 'data_nascimento']
    list_filter = ['nome', 'cpf', 'data_nascimento']
    change_list_filter_template = "admin/filter_listing.html"

admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Bairro)
admin.site.register(Municipio)
admin.site.register(Estado)
admin.site.register(Pais)
admin.site.register(TipoTelefone)
admin.site.register(Regiao)

# Register your models here.
