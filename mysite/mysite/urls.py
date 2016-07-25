
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import RedirectView

# from newsletter.views import ProfileImageIndexView

from django.contrib import admin
admin.autodiscover()

# from newsletter.views import ProfileImageView, ProfileDetailView
urlpatterns = [ 

	# url(r'^$', 'newsletter.views.home', name='home'),
	# url(r'^contact$', 'newsletter.views.contact', name='contact'),
 #    url(r'^upload/', ProfileImageView.as_view(), name='profile_image_upload'),
 #    url(
 #        r'^uploaded/(?P<pk>\d+)/$', ProfileDetailView.as_view(),
 #        name='profile_image'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/login/$','mysite.views.login'),
    url(r'^accounts/auth/$','mysite.views.auth_view'),
    url(r'^accounts/logout/$','mysite.views.logout'),
    url(r'^accounts/loggedin/$','mysite.views.loggedin'),
    url(r'^accounts/invalid/$','mysite.views.invalid_login'),
    url(r'^accounts/register/$','mysite.views.register_user'),
    url(r'^accounts/register_success/$','mysite.views.register_success'),
    url(r'^file_upload/', include('file_upload.urls') ),
    url(r'^delete/(?P<document_id>\d+)/$','file_upload.views.delete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)