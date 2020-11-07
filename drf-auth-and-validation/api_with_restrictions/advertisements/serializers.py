from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at',)

    def create(self, validated_data):
        """Метод для создания"""

        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
        validated_data["creator"] = self.context["request"].user

        if Advertisement.objects.all().filter(creator=validated_data["creator"], status="OPEN").count() > 4:
            raise ValidationError({"title": "превышен лимит активных объявлений"})

        if not validated_data["title"]:
            raise ValidationError({"title": "Не указано название товара"})

        if Advertisement.objects.all().filter(title=validated_data["title"]):
            raise ValidationError({"title": "Такое объявление уже существует"})

        return super().create(validated_data)

    def validate(self, data):
        pass
        return data
