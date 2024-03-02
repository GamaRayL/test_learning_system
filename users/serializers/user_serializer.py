from users.models import User
from main.models import Product
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField


class BaseUserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')


class UserProductSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field='email', read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'cost', 'author')


class UserDetailSerializer(ModelSerializer):
    products = SerializerMethodField()

    class Meta:
        model = User
        fields = ('email', 'products')

    @staticmethod
    def get_products(obj):
        products = obj.products.all()
        serialized_products = UserProductSerializer(products, many=True).data
        return serialized_products


class UserUpdateSerializer(BaseUserSerializer):
    pass


class UserListSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'role')
