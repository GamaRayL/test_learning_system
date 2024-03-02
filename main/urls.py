from django.urls import path

from main.apps import MainConfig
from main.views import ProductListAPIView, ProductCreateAPIView, ProductUpdateAPIView

app_name = MainConfig.name

urlpatterns = [
    # Product эндпоинты
    path('products/', ProductListAPIView.as_view(), name='products'),
    path('products/create/', ProductCreateAPIView.as_view(), name='product_create'),
    path('products/update/<int:pk>/', ProductUpdateAPIView.as_view(), name='product_update'),
]
