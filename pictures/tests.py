from django.test import TestCase
from .models import Editor,Pictures,Location,Category

class EditorTestClass(TestCase):
    #setup method
    def setUp(self):
        self.james=Editor(first_name='james',last_name='Muriuki', email='james@moringaschool.com')
        
        #Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Editor))

    #testing save method
    def test_save_method(self):
        self.james.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors)> 0)
        
class LocationTestClass(TestCase):
    #setup method
    def setUp(self):
        self.nakuru = Location(location_name='nakuru')
        #testing instance
    def test_instance(self):    
        self.assertTrue(isinstance(self.nakuru,Location))
        
        #save method test
    def test_save_method(self):
        self.nakuru.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)  
           
class CategoryTestClass(TestCase):
    def setUp(self):
        self.food = Category(category_name='food')
        #testing instance
    def test_instance(self):    
        self.assertTrue(isinstance(self.food,Category))
        
        #save method test
    def test_save_method(self):
        self.food.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)>0)
            