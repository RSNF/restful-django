from django.db import models
from .Categoria import Categoria
from .Autor import Autor

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    publicado_em = models.DateField()

    class Meta:
        ordering = ("titulo",)

    def __str__(self):
        return self.titulo
