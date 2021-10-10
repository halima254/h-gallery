from django.contrib import admin

# Register your models here.
from .models import Category, Editor, Pictures, Location

admin.site.register(Editor)
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Pictures)