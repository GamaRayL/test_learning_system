from main.models import Product
from rest_framework.serializers import ModelSerializer


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'start_datetime', 'cost', 'author')
