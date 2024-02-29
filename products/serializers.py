from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer

from products.models import Product


class ProductSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field='email', read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'cost', 'author')
