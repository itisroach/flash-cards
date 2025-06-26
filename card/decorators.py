from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from card.models import Card


def check_user_permissions(func):
    
    def wraper(request, *args, **kwargs):

        if not request.user.is_authenticated:

            return Response({"message": "you are not authorized, please login"}, status=status.HTTP_401_UNAUTHORIZED)
        
        elif request.method == "POST" and request.user.id == request.data["user"]:

            return func(request, *args, **kwargs)
        
        
        elif request.method in ("DELETE", "PUT"):

            card_id = kwargs.get("id")            
            
            card_obj = get_object_or_404(Card, id=card_id)

            if card_obj.user.id == request.user.id:

                return func(request, *args, **kwargs)
            
            elif card_obj.user.id != request.user.id:

                return Response({"message": "you are not authroized to perform this action"}, status=status.HTTP_403_FORBIDDEN)

            else:
                return card_obj
        
        elif request.method == "GET":
            return func(request, *args, **kwargs)

        else:
            return Response({"message": "you are not authroized to perform this action"}, status=status.HTTP_403_FORBIDDEN)

    return wraper
