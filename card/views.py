from django.shortcuts import render
from rest_framework.views import APIView
from card.serializers import CardSerializer
from rest_framework.response import Response
from rest_framework import status
from card.decorators import check_user_permissions
from django.utils.decorators import method_decorator


@method_decorator(check_user_permissions, name="post")
class CreateCardView(APIView):


    def post(self, request):

        req_data = request.data

        serializer = CardSerializer(data=req_data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

