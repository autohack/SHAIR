from django.conf.urls import patterns, url

urlpatterns = patterns('file_upload.views',
    url(r'^', 'list', name='list'),
)