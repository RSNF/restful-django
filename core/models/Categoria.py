from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        ordering = ("nome",)

    def __str__(self):
        return self.nome
