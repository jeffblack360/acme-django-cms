from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'cms.views.index'),
    url(r'^cms/', include('cms.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
