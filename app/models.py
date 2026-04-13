from django.db import models

# ------------------ CIDADE ------------------
class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.nome} - {self.uf}"


# ------------------ OCUPAÇÃO ------------------
class Ocupacao(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


# ------------------ PESSOA ------------------
class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    pai = models.CharField(max_length=100)
    mae = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    data_nasc = models.DateField()
    email = models.CharField(max_length=100)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


# ------------------ INSTITUIÇÃO ------------------
class InstituicaoEnsino(models.Model):
    nome = models.CharField(max_length=100)
    site = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


# ------------------ ÁREA DO SABER ------------------
class AreaSaber(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Área do Saber"
        verbose_name_plural = "Áreas do Saber"


# ------------------ CURSO ------------------
class Curso(models.Model):
    nome = models.CharField(max_length=100)
    carga_horaria_total = models.IntegerField()
    duracao_meses = models.IntegerField()
    area = models.ForeignKey(AreaSaber, on_delete=models.CASCADE)
    instituicao = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


# ------------------ DISCIPLINA ------------------
class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    area = models.ForeignKey(AreaSaber, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


# ------------------ MATRÍCULA ------------------
class Matricula(models.Model):
    instituicao = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_previsao_termino = models.DateField()

    def __str__(self):
        return f"{self.pessoa} - {self.curso}"
    
# ------------------ TURNO ------------------
class Turno(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


# ------------------ TURMA ------------------
class Turma(models.Model):
    nome = models.CharField(max_length=50)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} - {self.curso.nome}"


# ------------------ TIPO DE AVALIAÇÃO ------------------
class TipoAvaliacao(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


# ------------------ AVALIAÇÃO ------------------
class Avaliacao(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoAvaliacao, on_delete=models.CASCADE)
    nota = models.FloatField()

    def __str__(self):
        return f"{self.pessoa} - {self.nota}"

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"

# ------------------ FREQUÊNCIA ------------------
class Frequencia(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    presenca = models.BooleanField()
    data = models.DateField()

    def __str__(self):
        return f"{self.pessoa} - {self.data}"


# ------------------ OCORRÊNCIA ------------------
class Ocorrencia(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    descricao = models.TextField()
    data = models.DateField()

    def __str__(self):
        return f"{self.pessoa} - {self.data}"