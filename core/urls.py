from django.urls import path, include
from core.views import LivroView, AutorView, CategoriaView, ColecaoView
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r"livros", LivroView, basename="livros")
router.register(r"autores", AutorView, basename="autores")
router.register(r"categorias", CategoriaView, basename="categorias")
router.register(r"colecoes", ColecaoView, basename="colecoes")

urlpatterns = [path("", include(router.urls))]
