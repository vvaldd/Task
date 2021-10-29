from django.contrib.auth import get_user_model
from rest_framework import serializers

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    # create UserSerializer
    class Meta:
        model = UserModel
        fields = ('id', 'username', 'first_name', 'last_name', 'password', 'email', 'user_type')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        return UserModel.objects.create_user(**validated_data)




