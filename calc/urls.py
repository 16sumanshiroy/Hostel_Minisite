from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path("Home",views.Home,name='Home'),
    path("about",views.about,name='about'),
    path('services',views.services,name='services'),
    path('contacts',views.contact,name='contacts')  
]