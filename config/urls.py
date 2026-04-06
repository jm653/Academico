from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    # ADMIN
    path('admin/', admin.site.urls),

    # HOME
    path('', IndexView.as_view(), name='index'),

    # PESSOA
    path('pessoa/', PessoaView.as_view(), name='pessoa'),
    path('pessoa/create/', CreatePessoaView.as_view(), name='create_pessoa'),

    # CURSO
    path('curso/', CursoView.as_view(), name='curso'),

    # DISCIPLINA
    path('disciplina/', DisciplinaView.as_view(), name='disciplina'),

    # INSTITUIÇÃO
    path('instituicao/', InstituicaoView.as_view(), name='instituicao'),

    # CIDADE
    path('cidade/', CidadeView.as_view(), name='cidade'),

    # TURMA
    path('turma/', TurmaView.as_view(), name='turma'),

    # FREQUÊNCIA
    path('frequencia/', FrequenciaView.as_view(), name='frequencia'),

    # AVALIAÇÃO
    path('avaliacao/', AvaliacaoView.as_view(), name='avaliacao'),

    # TIPO DE AVALIAÇÃO
    path('tipo-avaliacao/', TipoAvaliacaoView.as_view(), name='tipo_avaliacao'),

    # OCORRÊNCIA
    path('ocorrencia/', OcorrenciaView.as_view(), name='ocorrencia'),
]