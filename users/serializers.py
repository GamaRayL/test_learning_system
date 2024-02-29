from rest_framework.serializers import ModelSerializer

from users.models import User


class BaseUserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')


class UserDetailSerializer(BaseUserSerializer):
    pass


class UserUpdateSerializer(BaseUserSerializer):
    pass


class UserListSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'role')
