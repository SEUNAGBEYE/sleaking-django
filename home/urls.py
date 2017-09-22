from django.conf.urls import url
from home.views import HomeView
from home.views import change_friend

urlpatterns  = [
	url(r'^$', HomeView.as_view(), name = 'home'),
	url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', change_friend, name = 'change_friend'),
]