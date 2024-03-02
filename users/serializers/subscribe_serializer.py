from rest_framework.serializers import ModelSerializer

from users.models import Subscribe


class SubscribeSerializer(ModelSerializer):
    class Meta:
        model = Subscribe
        fields = '__all__'
