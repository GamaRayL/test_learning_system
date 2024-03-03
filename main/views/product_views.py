from users.models import User
from main.models import Product
from rest_framework import status
from django.http import JsonResponse
from main.serializers.product_serializer import ProductSerializer
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView


class ProductCreateAPIView(CreateAPIView):
    """Создание продукта."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateAPIView(UpdateAPIView):
    """Обновление продукта."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListAPIView(ListAPIView):
    """Список продуктов."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


def add_user_to_product(request, pk_product, pk_user):
    """Добавление пользователя к продукту."""
    try:
        product = Product.objects.get(pk=pk_product)
        user = User.objects.get(pk=pk_user)

        if user in product.users.all():
            return JsonResponse(
                {'error': f'Пользователь ({user.email}) уже был добавлен к продукту: {product.name}!'},
                status=status.HTTP_400_BAD_REQUEST
            )

        product.users.add(user)

        return JsonResponse({'success': f'Пользователь ({user.email}) успешно добавлен к продукту: {product.name}!'})
    except Product.DoesNotExist:
        return JsonResponse(
            {'error': 'Такого продукта нет!'},
            status=status.HTTP_404_NOT_FOUND
        )
    except User.DoesNotExist:
        return JsonResponse(
            {'error': 'Такого пользователя нет!'},
            status=status.HTTP_404_NOT_FOUND
        )



