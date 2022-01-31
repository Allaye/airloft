from rest_framework import serializers
from account.models import User


class RegisterApiViewSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=125, min_length=5, write_only=True)


    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'is_staff')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
