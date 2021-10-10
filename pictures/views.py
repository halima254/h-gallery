from django.shortcuts import render
from django.http import HttpResponse
from .models import Editor, Pictures, Location, a

# Create your views here.
def welcome(request):
    return HttpResponse('welcome to my Gallery!')
