from django.shortcuts import render, redirect
from django.views import View
from .models import *
from .forms import PessoaForm


# ------------------ HOME ------------------
class IndexView(View):
    def get(self, request):
        pessoas = Pessoa.objects.all()
        return render(request, 'index.html', {'pessoas': pessoas})

# ------------------ PESSOA ------------------
class PessoaView(View):
    def get(self, request):
        pessoas = Pessoa.objects.select_related('cidade', 'ocupacao').all()
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
        cursos = Curso.objects.select_related('instituicao', 'area').all()
        return render(request, 'curso.html', {'cursos': cursos})


# ------------------ DISCIPLINA ------------------
class DisciplinaView(View):
    def get(self, request):
        disciplinas = Disciplina.objects.select_related('area').all()
        return render(request, 'disciplina.html', {'disciplinas': disciplinas})


# ------------------ INSTITUIÇÃO ------------------
class InstituicaoView(View):
    def get(self, request):
        instituicoes = InstituicaoEnsino.objects.select_related('cidade').all()
        return render(request, 'instituicao.html', {'instituicoes': instituicoes})


# ------------------ CIDADE ------------------
class CidadeView(View):
    def get(self, request):
        cidades = Cidade.objects.all()
        return render(request, 'cidade.html', {'cidades': cidades})


# ------------------ TURMA ------------------
class TurmaView(View):
    def get(self, request):
        turmas = Turma.objects.select_related('curso', 'turno').all()
        return render(request, 'turma.html', {'turmas': turmas})


# ------------------ FREQUÊNCIA ------------------
class FrequenciaView(View):
    def get(self, request):
        frequencias = Frequencia.objects.select_related('pessoa', 'disciplina').all()
        return render(request, 'frequencia.html', {'frequencias': frequencias})


# ------------------ AVALIAÇÃO ------------------
class AvaliacaoView(View):
    def get(self, request):
        avaliacoes = Avaliacao.objects.select_related('pessoa', 'disciplina', 'tipo').all()
        return render(request, 'avaliacao.html', {'avaliacoes': avaliacoes})


# ------------------ TIPO DE AVALIAÇÃO ------------------
class TipoAvaliacaoView(View):
    def get(self, request):
        tipos = TipoAvaliacao.objects.all()
        return render(request, 'tipo_avaliacao.html', {'tipos': tipos})


# ------------------ OCORRÊNCIA ------------------
class OcorrenciaView(View):
    def get(self, request):
        ocorrencias = Ocorrencia.objects.select_related('pessoa').all()
        return render(request, 'ocorrencia.html', {'ocorrencias': ocorrencias})
# ------------------ ÁREA DO SABER ------------------
class AreaSaberView(View):
    def get(self, request):
        areas = AreaSaber.objects.all()
        return render(request, 'area_saber.html', {'areas': areas})


# ------------------ MATRÍCULA ------------------
class MatriculaView(View):
    def get(self, request):
        matriculas = Matricula.objects.all()
        return render(request, 'matricula.html', {'matriculas': matriculas})


# ------------------ OCUPAÇÃO ------------------
class OcupacaoView(View):
    def get(self, request):
        ocupacoes = Ocupacao.objects.all()
        return render(request, 'ocupacao.html', {'ocupacoes': ocupacoes})
    
class UpdatePessoaView(View):
    def get(self, request, id):
        pessoa = Pessoa.objects.get(id=id)
        form = PessoaForm(instance=pessoa)
        return render(request, 'create_pessoa.html', {'form': form})

    def post(self, request, id):
        pessoa = Pessoa.objects.get(id=id)
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'create_pessoa.html', {'form': form})
    
class DeletePessoaView(View):
    def get(self, request, id):
        pessoa = Pessoa.objects.get(id=id)
        pessoa.delete()
        return redirect('index')