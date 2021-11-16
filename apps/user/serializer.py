from django.contrib.auth import get_user_model
from rest_framework import serializers
from core.validators.custom_validator import validate

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    # create UserSerializer

    # validated password
    password = serializers.CharField(validators=[validate])

    class Meta:
        model = UserModel
        fields = ('id', 'username', 'first_name', 'last_name', 'password', 'email', 'user_type')

    def create(self, validated_data):
        return UserModel.objects.create_user(**validated_data)

    # hidden password
    def to_representation(self, validated_data):
        representation = super(UserSerializer, self).to_representation(validated_data)
        representation.pop('password', None)
        return representation




