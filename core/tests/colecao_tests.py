from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from core.models import Colecao, Autor, Categoria, Livro


class ColecaoTests(APITestCase):
    def create_user_and_set_token_credentials(self):
        self.user = User.objects.create_user(
            "user01", "user01@example.com", "user01P4ssw0rD"
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token {0}".format(self.token.key))
        self.client.login(username="user01", password="user01P4ssw0rD")

    def setUp(self):
        self.create_user_and_set_token_credentials()

        categoria = Categoria.objects.create(nome="Categoria 1")
        autor = Autor.objects.create(nome="Autor 1")
        self.livro = Livro.objects.create(
            titulo="Foobar", autor=autor, categoria=categoria, publicado_em="2000-01-01"
        )

        self.colecao = Colecao.objects.create(
            nome="Coleção 1", descricao="Coleção 1 de 1", colecionador=self.user
        )

        self.colecao_post = {
            "nome": "Coleção 2",
            "descricao": "Coleção 2 de 2",
            "livros": [],
        }
        self.colecao_patch = {
            "livros": [reverse("core:livros-detail", {self.livro.pk})]
        }

    def test_create_collection(self):
        url = reverse("core:colecoes-list")
        authorized_post_response = self.client.post(
            url, self.colecao_post, format="json"
        )
        assert authorized_post_response.status_code == status.HTTP_201_CREATED
        assert authorized_post_response.data["nome"] == self.colecao_post["nome"]

    def test_get_collections(self):
        url = reverse("core:colecoes-detail", {self.colecao.pk})
        authorized_get_response = self.client.get(url, format="json")
        assert authorized_get_response.status_code == status.HTTP_200_OK
        assert authorized_get_response.data["nome"] == self.colecao.nome

    def test_add_books_to_collection(self):
        url = reverse("core:colecoes-detail", {self.colecao.pk})
        authorized_patch_response = self.client.patch(
            url, self.colecao_patch, format="json"
        )
        assert authorized_patch_response.status_code == status.HTTP_200_OK
        assert authorized_patch_response.data["nome"] == self.colecao.nome
