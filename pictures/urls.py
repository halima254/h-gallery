from django.conf.urls import url
from . import  views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', view.index,name='index'),
    url(r'^location/(\d+)', view.pictures_location,name='location'),
    url(r'^category/(\d+)', view.pictures_category,name='category'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)