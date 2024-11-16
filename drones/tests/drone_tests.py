from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status


class DroneCategoryTests(APITestCase):
    def post_drone_category(self, name):
        url = reverse("drones:dronecategory-list")
        data = {"name": name}
        response = self.client.post(url, data, format="json")
        return response

    def test_post_and_get_drone_category(self):
        new_drone_category_name = "Hexacopter"
        response = self.post_drone_category(new_drone_category_name)
        print(f"foo {response.data}")
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["name"] == new_drone_category_name

    def test_post_existing_drone_category_name(self):
        new_drone_category_name = "Duplicated Copter"
        response1 = self.post_drone_category(new_drone_category_name)
        assert response1.status_code == status.HTTP_201_CREATED
        response2 = self.post_drone_category(new_drone_category_name)
        assert response2.status_code == status.HTTP_400_BAD_REQUEST

    def test_get_drone_categories_collection(self):
        new_drone_category_name = "Super Copter"
        self.post_drone_category(new_drone_category_name)
        url = reverse("drones:dronecategory-list")
        response = self.client.get(url, format="json")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 1
        assert response.data["results"][0]["name"] == new_drone_category_name

    def test_update_drone_category(self):
        drone_category_name = "Category Initial Name"
        response = self.post_drone_category(drone_category_name)
        url = reverse("drones:dronecategory-detail", args=[response.data["id"]])
        update_drone_category_name = "Updated Name"
        data = {"name": update_drone_category_name}
        patch_response = self.client.patch(url, data, format="json")
        assert patch_response.status_code == status.HTTP_200_OK
        assert patch_response.data["name"] == update_drone_category_name
