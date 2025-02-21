from django.http import HttpResponse
from django.shortcuts import render
from .models import Hostels
# Create your views here.

def index(request):
    return HttpResponse("Welcome to my hostel")


def list_hostels(request):
    hostels = Hostels.objects.all()
    context = {'hotels':hostels}
    return render(request, 'hostels/list_hostels.html', context)