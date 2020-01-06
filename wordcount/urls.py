from . import views
from django.urls import path

urlpatterns = [
    path('', views.homepage,name='home'),
    path('contact/',views.contact,name='contact'),
    path('count/',views.count,name="countt")
    
]
