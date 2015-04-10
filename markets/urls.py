from django.conf.urls import patterns, include, url
from django.contrib import admin
from stocks import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'markets.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.search, name='search'),
    url(r'^stocks/', include('stocks.urls', namespace="stocks")),
    url(r'^admin/', include(admin.site.urls)),
)
