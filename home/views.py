from django.shortcuts import render
from .serializers import *
from .models import *
# Create your views here.
from rest_framework import generics

class GenericAddOrRead(generics.ListAPIView, generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialzer


class GenericeUpdateAndDelete(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset  = User.objects.all()
    serializer_class = UserSerialzer
    lookup_field = "id"


class CarAddorRead(generics.ListAPIView, generics.CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarDeleteorUpdate(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_field = 'id'
    

class AdsAddOrRead(generics.ListAPIView, generics.CreateAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer

class AddUpdateAndDelete(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer
    lookup_field = "id"

