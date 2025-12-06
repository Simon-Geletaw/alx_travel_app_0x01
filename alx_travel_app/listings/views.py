from rest_framework.views import APIView, Response, status
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserSerializer


class UserCreateView(APIView):    
    def get(self, request):
        serialgetdata = UserSerializer()
        user = serialgetdata.getdata(serialgetdata)
        return Response(user, status=status.HTTP_200_OK)
    
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            
            serializer.create(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    def login(self, request=UserSerializer.authenticate):
        return render(request, 'login.html')

    

 
