from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', IndexView.as_view(), name='index'),
    path('pessoa/', PessoaView.as_view(), name='pessoa'),
    path('curso/', CursoView.as_view(), name='curso'),
    path('disciplina/', DisciplinaView.as_view(), name='disciplina'),
    path('instituicao/', InstituicaoView.as_view(), name='instituicao'),
    path('cidade/', CidadeView.as_view(), name='cidade'),
]