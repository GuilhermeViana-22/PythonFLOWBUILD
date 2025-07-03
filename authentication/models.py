from django.db import models


class Usuario(models.Model):
    """Modelo simples de usuário para utilização com MySQL."""

    nome = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.email
