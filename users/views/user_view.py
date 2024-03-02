from users.models import User
from rest_framework import status
from rest_framework.response import Response
from users.serializers import UserSerializer, UserListSerializer, UserDetailSerializer, UserUpdateSerializer
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListAPIView


class UserCreateAPIView(CreateAPIView):
    """Создание пользователя."""
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = User.objects.create_user(
            email=serializer.validated_data['email'],
            password=serializer.validated_data['password']
        )
        user.save()

        return user


class UserListAPIView(ListAPIView):
    """Список пользователей."""
    serializer_class = UserListSerializer
    queryset = User.objects.all()


class UserDetailAPIView(RetrieveAPIView):
    """Детализация пользователя."""
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(UpdateAPIView):
    """Обновление пользователя."""
    serializer_class = UserUpdateSerializer
    queryset = User.objects.all()


class UserDeleteAPIView(DestroyAPIView):
    """Удаление пользователя."""
    queryset = User.objects.all()

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return Response(
            {'message': 'Пользователь удалён.'},
            status=status.HTTP_204_NO_CONTENT
        )

