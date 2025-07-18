from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model

class UserSerializer(ModelSerializer):
    class Meta:
        model        = get_user_model()
        fields       = ("id", "username", "email" ,"password", "date_joined")
        read_only_fields = ('date_joined', 'id')
        extra_kwargs = {
            'password': {'write_only': True},
        }
