from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^location/(\d+)', views.pictures_location,name='location'),
    url(r'^category/(\d+)', views.pictures_category,name='category'),
    url(r'^single_pic/(\d+)', views.single_picture,name='single_pic'),
    url(r'^search/', views.search_picture,name='search_results'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)