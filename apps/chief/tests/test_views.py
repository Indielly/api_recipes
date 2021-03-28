import pytest
from rest_framework.test import APIClient
from django.urls import reverse


@pytest.mark.django_db
class TestChiefViewSets:

    client = APIClient()

    def test_should_create_new_chief(self):
        data = {
            "first_name": "Indielly",
            "last_name": "Barbosa",
            "username": "Indy",
            "email": "bindielly@gmail.com",
            "password": "indy123456"
        }

        response = self.client.post(reverse("chief-list"), data=data, format="json")
        
        assert response.status_code == 201

        assert response.json()["first_name"] == data["first_name"]
        assert response.json()["last_name"] == data["last_name"]
        assert response.json()["username"] == data["username"]
        assert response.json()["email"] == data["email"]
        