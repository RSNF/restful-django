from django.urls import path
from core.views.LivrosView import LivroView

urlpatterns = [
    path('livros/', LivroView.as_view()),
    path('livros/<int:id>', LivroView.as_view())
]
