from django.db import models

# Create your models here.

class MotivoContato(models.Model):
    nome = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nome
    



class fale_conosco(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length = 20)
    motivoContato = models.ForeignKey(MotivoContato,on_delete=models.DO_NOTHING)
    assunto = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.nome
    

class aluguel(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    telefoneFixo = models.CharField(max_length = 20)
    telefoneCel = models.CharField(max_length = 20)
    
    
    def __str__(self):
        return self.nome
    

class cliente(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.IntegerField(max_length = 11)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length = 20)
    
    
    
    def __str__(self):
        return self.nome