from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from apps.recipe.models import Recipe
from apps.recipe.serializers import RecipeSerializer


class RecipeViewSet(ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ["ingredients", "preparation", "chief__first_name"]
    filterset_fields = ["name", "preparation_time"]  # filtro de pesquisa
    permission_classes = [IsAuthenticated]
    permission_classes_by_action = {  # permissão por ação
        "list": [AllowAny],
    }

    def get_permissions(self):
        try:
            return [
                permission()
                for permission in self.permission_classes_by_action[self.action]
            ]
        except KeyError:
            return [permission() for permission in self.permission_classes]
