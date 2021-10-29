from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializer import UserSerializer

UserModel: User = get_user_model()


class UserListCreateView(ListCreateAPIView):
    # create class for list/create
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    # create class for retrieve/delete/update
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
