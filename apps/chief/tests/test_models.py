import pytest

from apps.chief.models import Chief


@pytest.mark.django_db
class TestChiefModel:
    def test_should_return_chief_name_in_str(self):
        chief = Chief.objects.create(
            first_name="Indielly",
            last_name="Barbosa",
            username="indy",
            email="bindielly@gmail.com",
        )

        expected_value = "Indielly Barbosa"

        assert chief.__str__() == expected_value
