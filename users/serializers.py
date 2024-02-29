from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from products.models import Product
from products.serializers import ProductSerializer
from users.models import User


class BaseUserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')


class UserDetailSerializer(ModelSerializer):
    products = SerializerMethodField()

    class Meta:
        model = User
        fields = ('email', 'products')

    @staticmethod
    def get_products(obj):
        products = obj.products.all()
        serialized_products = ProductSerializer(products, many=True).data
        return serialized_products


class UserUpdateSerializer(BaseUserSerializer):
    pass


class UserListSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'role')
