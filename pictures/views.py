from django.shortcuts import render
from django.http import HttpResponse
from .models import Editor, Pictures, Location, Category

# Create your views here.
def welcome(request):
    return HttpResponse('welcome to my Gallery!')


def index(request):
    pictures = Pictures.all_pictures()
    category = Category.get_category()
    location = Location.get_location()
    
    return render(request, 'index.html',{'pictures':pictures,'category':category,'location':location})

def pictures_location(request,location):
    location_pictures = Pictures.picture_bylocation(location)
    
    return render(request,'location.html',{'location_pictures':location_pictures} )

def pictures_category(request,category):
    category_pictures = Pictures.picture_bycategory(category)
    
    return render(request,'category.html',{'category_pictures':category_pictures} )


    
