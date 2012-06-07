from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'browser_map_red.views.home', name='home'),
    # url(r'^browser_map_red/', include('browser_map_red.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'map_red.views.index', name='index'),
    url(r'^emit/reduce?$', "map_red.views.reduce", name="reduce"),
    url(r'^emit/finalize?$', "map_red.views.finalize", name="finalize")
)
