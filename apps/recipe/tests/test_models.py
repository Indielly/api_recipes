import pytest
from apps.recipe.models import Recipe
from apps.chief.models import Chief


@pytest.mark.django_db
class TestRecipeModel:

    def test_should_return_recipe_name_in_str_method(self):
        chief = Chief.objects.create(
            first_name="Indielly",
            last_name="Barbosa",
            username="indy",
            email="bindielly@gmail.com",
        )

        recipe = Recipe.objects.create(
            name="Test recipe",
            ingredients="test ingredients.....",
            preparation="test_preparation",
            preparation_time='00:10',
            chief=chief
        )

        expected_value = "Test recipe"

        assert recipe.__str__() == expected_value