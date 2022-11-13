from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h3>Lightness Web Server</h3><br/><h4>Click <a href='/webapp'>HERE</a></h4>")