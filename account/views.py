from rest_framework import status
from rest_framework.views import APIView
from .serializers import AccountSerializer
from rest_framework.response import Response
import sys

# Create your views here.
class CurrentUserView(APIView):

    def post(self,request):
        serializer=AccountSerializer(request.user)
        return Response(serializer.data,status=status.HTTP_200_OK)
