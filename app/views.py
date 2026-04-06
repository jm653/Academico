from django.shortcuts import render, redirect
from django.views import View
from .models import *
from .forms import PessoaForm


# ------------------ HOME ------------------
class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


# ------------------ PESSOA ------------------
class PessoaView(View):
    def get(self, request):
        pessoas = Pessoa.objects.all()
        return render(request, 'pessoa.html', {'pessoas': pessoas})


class CreatePessoaView(View):
    def get(self, request):
        form = PessoaForm()
        return render(request, 'create_pessoa.html', {'form': form})

    def post(self, request):
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pessoa')
        return render(request, 'create_pessoa.html', {'form': form})


# ------------------ CURSO ------------------
class CursoView(View):
    def get(self, request):
        cursos = Curso.objects.all()
        return render(request, 'curso.html', {'cursos': cursos})


# ------------------ DISCIPLINA ------------------
class DisciplinaView(View):
    def get(self, request):
        disciplinas = Disciplina.objects.all()
        return render(request, 'disciplina.html', {'disciplinas': disciplinas})


# ------------------ INSTITUIÇÃO ------------------
class InstituicaoView(View):
    def get(self, request):
        instituicoes = InstituicaoEnsino.objects.all()
        return render(request, 'instituicao.html', {'instituicoes': instituicoes})


# ------------------ CIDADE ------------------
class CidadeView(View):
    def get(self, request):
        cidades = Cidade.objects.all()
        return render(request, 'cidade.html', {'cidades': cidades})


# ------------------ TURMA ------------------
class TurmaView(View):
    def get(self, request):
        turmas = Turma.objects.all()
        return render(request, 'turma.html', {'turmas': turmas})


# ------------------ FREQUÊNCIA ------------------
class FrequenciaView(View):
    def get(self, request):
        frequencias = Frequencia.objects.all()
        return render(request, 'frequencia.html', {'frequencias': frequencias})


# ------------------ AVALIAÇÃO ------------------
class AvaliacaoView(View):
    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        return render(request, 'avaliacao.html', {'avaliacoes': avaliacoes})


# ------------------ TIPO DE AVALIAÇÃO ------------------
class TipoAvaliacaoView(View):
    def get(self, request):
        tipos = TipoAvaliacao.objects.all()
        return render(request, 'tipo_avaliacao.html', {'tipos': tipos})


# ------------------ OCORRÊNCIA ------------------
class OcorrenciaView(View):
    def get(self, request):
        ocorrencias = Ocorrencia.objects.all()
        return render(request, 'ocorrencia.html', {'ocorrencias': ocorrencias})