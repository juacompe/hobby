from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hobby.views.home', name='home'),
    # url(r'^hobby/', include('hobby.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
