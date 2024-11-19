from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from core.models import Colecao, Autor, Categoria, Livro


class ColecaoTests(APITestCase):
    def create_user_and_set_token_credentials(self):
        self.user_1 = User.objects.create_user(
            "user01", "user01@example.com", "user01P4ssw0rD"
        )
        self.user_2 = User.objects.create_user(
            "user02", "user02@example.com", "user02P4ssw0rD"
        )
        self.client.login(username="user01", password="user01P4ssw0rD")

    def login_user1(self):
        self.client.logout()
        self.client.login(username="user01", password="user01P4ssw0rD")

    def login_user2(self):
        self.client.logout()
        self.client.login(username="user02", password="user02P4ssw0rD")

    def setUp(self):
        self.create_user_and_set_token_credentials()

        categoria = Categoria.objects.create(nome="Categoria 1")
        autor = Autor.objects.create(nome="Autor 1")
        self.livro = Livro.objects.create(
            titulo="Foobar", autor=autor, categoria=categoria, publicado_em="2000-01-01"
        )

        self.colecao = Colecao.objects.create(
            nome="Coleção 1", descricao="Coleção 1 de 1", colecionador=self.user_1
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

    def test_create_collection_2(self):
        self.client.logout()
        url = reverse("core:colecoes-list")
        authorized_post_response = self.client.post(
            url, self.colecao_post, format="json"
        )
        assert authorized_post_response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_get_collections(self):
        url = reverse("core:colecoes-detail", {self.colecao.pk})
        authorized_get_response = self.client.get(url, format="json")
        assert authorized_get_response.status_code == status.HTTP_200_OK
        assert authorized_get_response.data["nome"] == self.colecao.nome

    def test_add_books_to_collection(self):
        self.login_user1()
        url = reverse("core:colecoes-detail", {self.colecao.pk})
        authorized_patch_response = self.client.patch(
            url, self.colecao_patch, format="json"
        )
        assert authorized_patch_response.status_code == status.HTTP_200_OK
        assert authorized_patch_response.data["nome"] == self.colecao.nome

    def test_add_books_to_collection_2(self):
        self.login_user2()
        url = reverse("core:colecoes-detail", {self.colecao.pk})
        unauthorized_patch_response = self.client.patch(
            url, self.colecao_patch, format="json"
        )
        assert unauthorized_patch_response.status_code == status.HTTP_403_FORBIDDEN
