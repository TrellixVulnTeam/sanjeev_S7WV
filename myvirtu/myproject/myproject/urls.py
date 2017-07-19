"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from myapp import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^stocks/', views.StockList.as_view()),
    # url(r'^register/$', views.UserCreateAPIView.as_view()),
    # url(r'^login/$', views.UserLoginAPIView.as_view()),
    # url(r'^stockcreate/', views.StockCreate.as_view()),
    # url(r'^(?P<id>[\d+])/edit/$', views.StockUpdate.as_view()),
    # url(r'^(?P<id>[\d+])/delete/$', views.StockDelete.as_view()),
    # url(r'^api-auth/', include('rest_framework.urls',
                               # namespace='rest_framework')),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)