from rest_framework.views import APIView
from card.serializers import CardSerializer, UpdateCardSerializer
from rest_framework.response import Response
from rest_framework import status
from card.decorators import check_user_permissions
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404, get_list_or_404
from card.models import Card


@method_decorator(check_user_permissions, name="post")
class CreateCardView(APIView):


    def post(self, request):

        req_data = request.data

        serializer = CardSerializer(data=req_data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

@method_decorator(check_user_permissions, name="put")
class UpdateCardView(APIView):

    def put(self, request, card_id):

        req_data = request.data

        card_obj = get_object_or_404(Card, id=card_id)

        serializer = UpdateCardSerializer(instance=card_obj, data=req_data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


@method_decorator(check_user_permissions, name="delete")
class DeleteCardView(APIView):

    def delete(self, request, card_id):
        
        instance = get_object_or_404(Card, id=card_id)

        instance.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
    

@method_decorator(check_user_permissions, name="get")
class GetUserCardsView(APIView):

    def get(self, request):
        
        card_list = get_list_or_404(Card, user__id=request.user.id)


        serializer = CardSerializer(card_list, many=True)


        return Response(serializer.data, status=status.HTTP_200_OK)
    


class GetSingleCardView(APIView):
    
    
    def get(self, request, card_id):

        card = get_object_or_404(Card, id=card_id)

        serializer = CardSerializer(card)

        return Response(serializer.data, status=status.HTTP_200_OK)