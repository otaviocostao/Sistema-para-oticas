from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(
        verbose_name="Nome", max_length=150, null=False, blank=False
    )

    telefone =  models.CharField(
        verbose_name="Telefone", max_length=15, null=False, blank=False
    )

    endereco = models.CharField(
        verbose_name="Endereço", max_length=150, null=False, blank=False
    )

    email = models.CharField(
        verbose_name="E-mail", max_length=70
    )

    cpf = models.CharField(
        verbose_name="CPF", max_length=14
    )

    data_nasc = models.DateField()
    
    objetos = models.Manager()