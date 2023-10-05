from django.db import models

class Morador(models.Model):
    nome = models.CharField(max_length=30)
    cpf = models.CharField(max_length=11)
    email = models.CharField(max_length=30)
    senha = models.CharField(max_length=20)
    celular = models.CharField(max_length=11)
    cep = models.CharField(max_length=8)
    rua = models.CharField(max_length=30)
    numero_casa = models.CharField(max_length=9)
    bairro = models.CharField(max_length=40)
    
    
    def __str__(self):
        return self.nome

class FaltouAgua(models.Model):
    RESPOSTAFALTA = (
        ("Sim", "Sim"),
        ("Não", "Não")
    )
    respostafalta = models.CharField(max_length=3, choices=RESPOSTAFALTA, blank=False, null=False, default="Sim")
    
    def __str__(self):
        return self.resposta
    
