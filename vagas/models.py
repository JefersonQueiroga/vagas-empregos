from django.db import models


class Funcao(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Função'
        verbose_name_plural = 'Funções'

    def __str__(self):
        return self.nome


class Empresa(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.nome


class Vaga(models.Model):
    data_cadastrado = models.DateField(auto_now_add=True)
    descricao_vaga = models.TextField()
    funcao = models.ForeignKey(Funcao, on_delete=models.CASCADE, related_name='vagas')
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='vagas')
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    qtd_vagas = models.IntegerField(verbose_name='Quantidade de Vagas')

    class Meta:
        verbose_name = 'Vaga'
        verbose_name_plural = 'Vagas'
        ordering = ['-data_cadastrado']

    def __str__(self):
        return f"{self.funcao.nome} - {self.empresa.nome}"
