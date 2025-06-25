from rest_framework.response import Response
from rest_framework import status


def check_user_permissions(func):
    
    def wraper(request, *args, **kwargs):
        
        if request.user.is_authenticated:
            return Response({"message": "you are not authorized"}, status=status.HTTP_401_UNAUTHORIZED)
        
        elif request.user.id == request.data["user"]:
            return func(request, *args, **kwargs)
        
        else:
            return Response({"message": "you are not authroized to perform this action"}, status=status.HTTP_403_FORBIDDEN)

    return wraper