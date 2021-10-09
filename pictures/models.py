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
    
class Pictures(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to ='pictures/')    
    editor = models.ForeignKey('Editor', on_delete = models.CASCADE)
    
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
    def all_pictures(cls,id):
        pictures = cls.objects.all()
        
        return pictures
    
    @classmethod
    def one_picture(cls,id):
        picture = cls.objects.filter(id=id)
        
        return picture
