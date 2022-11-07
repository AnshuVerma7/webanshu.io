from django.contrib import admin
from django.urls import path,include
from home import veiws

urlpatterns = [
    path('',views.index,name='hoome'),
    path('blog',views.blog,name='blog'),
    path('contact',views.intro,name='intro'),
    path('index',views.blog,name='blog'),
    path('intro',views.services,name='services'),
    path('services',views.contact,name='services'),
 
]
