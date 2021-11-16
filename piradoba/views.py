from django.shortcuts import render
from django.http import HttpResponse
from .models import identity

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})

def list_view(request, *args, **kwargs):
    obj = identity.objects.all()
    return render(request, 'list.html', {"obj":obj})