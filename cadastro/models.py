from django.db import models

# Create your models here.

class Loja(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)

