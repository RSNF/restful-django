from django.urls import path, include
from core.views import LivroView, AutorView, CategoriaView
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r"livros", LivroView)
router.register(r"autores", AutorView)
router.register(r"categorias", CategoriaView)

urlpatterns = [
    path("", include(router.urls))
]
