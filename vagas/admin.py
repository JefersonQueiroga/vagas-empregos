from django.contrib import admin
from .models import Funcao, Empresa, Vaga


@admin.register(Funcao)
class FuncaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone')
    search_fields = ('nome', 'email')


@admin.register(Vaga)
class VagaAdmin(admin.ModelAdmin):
    list_display = ('funcao', 'empresa', 'salario', 'qtd_vagas', 'data_cadastrado')
    list_filter = ('funcao', 'empresa', 'data_cadastrado')
    search_fields = ('descricao_vaga', 'funcao__nome', 'empresa__nome')
    date_hierarchy = 'data_cadastrado'
