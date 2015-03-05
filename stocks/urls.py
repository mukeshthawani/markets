from django.conf.urls import patterns, url

from stocks import views

urlpatterns = patterns('',
    url(r'^$', views.search, name='search'),
    url(r'^(?P<stocks_id>\d+)/$', views.data, name='data'),
    # url(r'^(?P<stocks_id>\d+)/(?P<choice_id>\d+)/$', views.data, name='data')
)
