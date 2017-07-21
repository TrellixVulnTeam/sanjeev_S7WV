from django.conf.urls import url,include
from django.contrib import admin
from .views import home
from .views import Contact
from .views import generate

urlpatterns = [
    
    url(r'^$',home),
    url(r'^me/$',Contact),
    url(r'^to/$',generate),

]