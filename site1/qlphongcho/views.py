from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate
# Create your views here.
def index(request):
    return HttpResponse("Hello word")
