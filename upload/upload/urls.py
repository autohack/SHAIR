"""upload URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.conf.urls import patterns, include, url
#from django.conf.urls.defaults import *
from django.conf.urls.static import static
from django.conf import settings

from file_upload.views import ProfileImageIndexView

from django.contrib import admin
admin.autodiscover()

from file_upload.views import ProfileImageView, ProfileDetailView

urlpatterns = patterns('',
    url(r'^$', ProfileImageIndexView.as_view(), name='home'),

    url(r'^upload/', ProfileImageView.as_view(), name='profile_image_form'),
    url(
        r'^uploaded/(?P<pk>\d+)/$', ProfileDetailView.as_view(),
        name='profile_image'),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
