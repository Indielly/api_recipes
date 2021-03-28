from rest_framework import serializers

from apps.chief.models import Chief


class ChiefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chief  # nome do aplicativo e nome do model
        fields = ["id","first_name", "last_name", "username", "email", "password"]
        extra_kwargs = {
            "password": {"write_only": True, "style": {"input_type": "password"}}
        }

    def create(self, validated_data):
        instance = Chief.objects.create(
            **validated_data
        )  # desempacotamento de dicionario
        instance.set_password(validated_data["password"])
        instance.save()
        return instance
