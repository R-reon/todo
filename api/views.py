from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .utils.auth import NormalAuthentication
from api.utils.auth import JWTAuthentication
from rest_framework import status


class Login(APIView):

    authentication_classes = [NormalAuthentication,]

    def post(self, request, *args, **kwargs):
        return Response({"token": request.user})

class Something(APIView):
    authentication_classes = [JWTAuthentication, ]
    # ログインしてるユーザーだけアクセスできるようにします。
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        # return Response({"data": "中身です"})
         return Response(data={'id':request.user.id, 'username': request.user.username, 'password':request.user.password}, status=status.HTTP_200_OK)