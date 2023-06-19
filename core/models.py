from django.db import models

# Create your models here.

class Carro(models.Model):
    placa = models.CharField(max_length=7)
    modelo = models.CharField(max_length=15)
    marca = models.CharField(max_length=15)
    cor = models.CharField(max_length=15)

    def __str__(self):
        return self.placa
