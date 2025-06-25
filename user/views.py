from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from user.serializers import UserSerializer
from rest_framework import status
from rest_framework.response import Response

User = get_user_model()

class RegisterUserView(APIView):

    def post(self, request):
        data = request.data

        serializer = UserSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        user_data = serializer.validated_data

        user_obj = User(
            username = user_data["username"],
            email    = user_data["email"]
        )

        user_obj.set_password(user_data["password"])

        user_obj.save()

        # to be returned the values of read_only fields in user serializer
        return Response(UserSerializer(user_obj).data, status=status.HTTP_201_CREATED)


