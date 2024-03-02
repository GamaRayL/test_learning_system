from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import Subscribe
from users.serializers import SubscribeSerializer
from users.services import assign_user_to_group


class SubscribeAPIView(APIView):
    @staticmethod
    def post(request):
        serializer = SubscribeSerializer(data=request.data)
        user = request.data.get('user')
        product = request.data.get('product')

        subscribe_instance = Subscribe.objects.filter(user=user, product=product).first()

        if subscribe_instance:
            assign_user_to_group(subscribe_instance)
            subscribe_instance.is_active = not subscribe_instance.is_active
            subscribe_instance.save()
            serializer = SubscribeSerializer(subscribe_instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            if serializer.is_valid():
                serializer.save()
                subscribe_instance = Subscribe.objects.filter(user=user, product=product).first()
                assign_user_to_group(subscribe_instance)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

