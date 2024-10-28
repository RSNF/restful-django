from django.urls import path, include
from core.views import LivroView, AutorView, CategoriaView
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r"livros", LivroView, basename="livros")
router.register(r"autores", AutorView, basename="autores")
router.register(r"categorias", CategoriaView, basename="categorias")

urlpatterns = [path("", include(router.urls))]
