from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from apps.chief.models import Chief
from apps.chief.serializers import ChiefSerializer


class ChiefViewSet(ModelViewSet):
    queryset = Chief.objects.all()  # coleção de dados que vem do banco de dados
    serializer_class = ChiefSerializer  # classe utilizada para conversão dos dados
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["first_name", "last_name", "username", "email"]  # filtrando
