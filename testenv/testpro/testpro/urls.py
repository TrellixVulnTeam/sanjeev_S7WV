"""testpro URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import ugettext_lazy as _
from testapp.views import Contact
from django.conf import settings
from django.conf.urls.static import static
# from testapp.views import Generate_Pdf
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^contact/',include('testapp.urls')),
    # url(r'^vw/',include("testapp.urls")),
    url(r'^pdf/',include('testapp.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



urlpatterns += i18n_patterns(
    
    url(r'^vw/',include("testapp.urls")),
    
    )

# admin.site.site_header = _('My project')
admin.site.index_title = _('Administration....')
# admin.site.site_title = _('HTML title from adminsitration')