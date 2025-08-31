from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
# from rest_framework.views import APIView
# from rest_framework.viewsets import ViewSet

from .models import Booking, MenuItem
from .serializers import BookingSerializer, MenuItemSerializer, UserSerializer
from django.contrib.auth.models import User


# Create your views here.

#Menu Items
class MenuItemsView(ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]

class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]

# Booking
class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


