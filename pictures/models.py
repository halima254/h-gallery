from django.db import models

# Create your models here
class Editor(models.Model):
    #edito class inherits from tje modules.Model class
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10,blank=True)
    
    def __str__(self):
        return self.first_name
    def save_editor(self):
        self.save()
    
class Pictures(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to ='pictures/')    
    editor = models.ForeignKey('Editor', on_delete = models.CASCADE)
    category= models.ForeignKey('Category',on_delete= models.CASCADE, default=None)
    location= models.ForeignKey('Location',on_delete= models.CASCADE, default=None)
    
                             
    def save_image(self):
        ''' 
        saving images
        '''
        self.save()
     
    def delete_image(self):
        '''
        delete images
        '''
        self.delete() 
           
    @classmethod
    def all_pictures(cls):
        pictures = cls.objects.all()
        
        return pictures
    
    @classmethod
    def one_picture(cls,id):
        picture = cls.objects.filter(id=id)
        
        return picture
    
    
    @classmethod
    def search_picture(cls,term):
        image = cls.objects.filter(name__icontains = term)
        
        return image
    
    @classmethod
    def picture_bylocation(cls,location):
        location_pictures= cls.objects.filter(location=location)
        return location_pictures
    
    
    @classmethod
    def picture_bycategory(cls,category):
        category_pictures= cls.objects.filter(category=category)
        return category_pictures
    
class Location(models.Model):
    location_name= models.CharField(max_length= 80)
    
    def save_location(self):
        self.save()
        
    @classmethod
    def get_location(cls):
        locations = cls.objects.all()
        return locations
        
    def __str__(self):
        return self.location_name
    
        
class Category(models.Model):
    category_name= models.CharField(max_length= 80)
    
    def save_category(self):
        self.save()
        
    @classmethod
    def get_category(cls):
        categories = cls.objects.all()
        return categories
        
    def __str__(self):
        return self.category_name
    
    