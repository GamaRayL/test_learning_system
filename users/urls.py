from django.urls import path

from users.apps import UsersConfig
from users.views import UserDeleteAPIView, UserUpdateAPIView, UserDetailAPIView, UserCreateAPIView, UserListAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('', UserListAPIView.as_view(), name='user_list'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('<int:pk>/', UserDetailAPIView.as_view(), name='user_detail'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update'),
    path('delete/<int:pk>/', UserDeleteAPIView.as_view(), name='user_delete')
]