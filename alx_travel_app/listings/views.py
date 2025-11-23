from rest_framework import generics
from .models import User
from .serializers import UserSerializer


class UserCreateView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save()
