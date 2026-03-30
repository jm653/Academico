from django.shortcuts import render
from django.views import View
from .models import *

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class PessoaView(View):
    def get(self, request):
        pessoas = Pessoa.objects.all()
        return render(request, 'pessoa.html', {'pessoas': pessoas})


class CursoView(View):
    def get(self, request):
        cursos = Curso.objects.all()
        return render(request, 'curso.html', {'cursos': cursos})


class DisciplinaView(View):
    def get(self, request):
        disciplinas = Disciplina.objects.all()
        return render(request, 'disciplina.html', {'disciplinas': disciplinas})


class InstituicaoView(View):
    def get(self, request):
        instituicoes = InstituicaoEnsino.objects.all()
        return render(request, 'instituicao.html', {'instituicoes': instituicoes})


class CidadeView(View):
    def get(self, request):
        cidades = Cidade.objects.all()
        return render(request, 'cidade.html', {'cidades': cidades})