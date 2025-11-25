from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    endereco = models.CharField(max_length=300)
    telefone = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.user.username
