from django.contrib import admin
from .models import *


# ------------------ INLINE ------------------

class MatriculaInline(admin.TabularInline):
    model = Matricula
    extra = 1


class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 1


class OcorrenciaInline(admin.TabularInline):
    model = Ocorrencia
    extra = 1


# ------------------ ADMIN PERSONALIZADO ------------------

class PessoaAdmin(admin.ModelAdmin):
    inlines = [MatriculaInline, AvaliacaoInline, OcorrenciaInline]


# ------------------ REGISTROS ------------------

admin.site.register(Pessoa, PessoaAdmin)

admin.site.register(Cidade)
admin.site.register(Ocupacao)
admin.site.register(InstituicaoEnsino)
admin.site.register(AreaSaber)
admin.site.register(Curso)
admin.site.register(Disciplina)
admin.site.register(Matricula)
admin.site.register(Turma)
admin.site.register(Turno)
admin.site.register(Frequencia)
admin.site.register(Ocorrencia)
admin.site.register(Avaliacao)
admin.site.register(TipoAvaliacao)