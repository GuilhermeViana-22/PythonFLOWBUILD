from django.db import models

class DashboardUser(models.Model):
    name = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, null=True, blank=True)
    email = models.CharField(max_length=255, unique=True)
    email_verified_at = models.DateTimeField(null=True, blank=True)
    password = models.CharField(max_length=128)
    data_nascimento = models.DateField(null=True, blank=True)
    telefone_celular = models.CharField(max_length=20)
    genero = models.CharField(max_length=20, null=True, blank=True)
    position_id = models.IntegerField(null=True, blank=True)
    unidade_id = models.IntegerField(null=True, blank=True)
    status_id = models.IntegerField(null=True, blank=True)
    foto_perfil = models.CharField(max_length=255, null=True, blank=True)
    ultimo_acesso = models.DateTimeField(null=True, blank=True)
    ativo = models.BooleanField(default=True)
    situacao_id = models.IntegerField(null=True, blank=True)
    remember_token = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name
