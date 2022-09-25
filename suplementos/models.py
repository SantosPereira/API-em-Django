from django.db import models

# Create your models here.
class Suplemento(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    marca = models.CharField(max_length=80)
    categoria = models.CharField(max_length=80)
    preco = models.IntegerField()

    def __str__(self):
        return self.nome
