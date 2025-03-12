from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializer import PlayerSerializer,Player,CustomerSerializer,Customer

# Create your views here.

def myfirstview(request):
    return HttpResponse('My first independent test')

class PlayerViewSet(ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer