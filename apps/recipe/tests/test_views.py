import pytest
from rest_framework.test import APIClient
from django.urls import reverse

from apps.chief.models import Chief


@pytest.mark.django_db
class TestRecipeViewSet:

    client = APIClient()

    def test_should_fail_if_try_create_recipe_without_authentication(self):
        chief = Chief.objects.create(
            first_name="Indielly",
            last_name="Barbosa",
            username="indy",
            email="bindielly@gmail.com",
        )

        data = {
            "name": "Test recipe",
            "ingredients": "Test ingredients...",
            "preparation": "Test preparation...",
            "preparation_time": '00:10',
            "chief": chief.id
        }

        response = self.client.post(reverse("recipe-list"), data, format="json")

        assert response.status_code == 403

    def test_should_create_a_recipe_successfully(self):
        chief = Chief.objects.create(
            first_name="Indielly",
            last_name="Barbosa",
            username="indy",
            email="bindielly@gmail.com",
        )
        chief.set_password("indy123")
        chief.save()

        chief.refresh_from_db()

        data = {
            "name": "Test recipe",
            "ingredients": "Test ingredients...",
            "preparation": "Test preparation...",
            "preparation_time": '00:10',
            "chief": chief.id
        }

        self.client.force_authenticate(user=chief)
        response = self.client.post(reverse("recipe-list"), data, format="json")

        assert response.status_code == 201

