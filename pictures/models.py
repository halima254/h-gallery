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
