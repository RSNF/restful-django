from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from drones.models import Pilot


class PilotTests(APITestCase):
    def create_user_and_set_token_credentials(self):
        user = User.objects.create_user(
            "user01", "user01@example.com", "user01P4ssw0rD"
        )
        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION="Token {0}".format(token.key))

    def setUp(self):
        self.create_user_and_set_token_credentials()
        self.pilot = Pilot.objects.create(
            name="Gaston", gender=Pilot.MALE, races_count=5
        )

    def test_get_pilots(self):
        url = reverse("drones:pilots-detail", {self.pilot.pk})
        authorized_get_response = self.client.get(url, format="json")
        assert authorized_get_response.status_code == status.HTTP_200_OK
        assert authorized_get_response.data["name"] == self.pilot.name
