from django.shortcuts import render
from django.http import HttpResponse,Http404
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

def single_picture(request,id):
    
    try:
        single_pic = Pictures.objects.get(id=id)
    
    except DoesNotExist:
        raise Http404()
    
    return render(request,'single_pic.html',{'single_pic':single_pic})    
    
def search_picture(request):
    
    if 'image' in request.GET and request.GET['image']:
        search_term = request.GET.get('image')
        search_image = Pictures.search_picture(term)
        message = f'{term}'
        
        return render(request,'get_image.html',{'message':message, 'search_image':search_image})
    
    else:
        message = 'Image not found'
        
        return render(request,'get_image.html',{'message':message})    