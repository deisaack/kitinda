from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.CentreList.as_view(), name='centre-list'),
	url(r'^(?P<pk>[0-9]+)/$', views.CentreDetailView.as_view(), name='centre-detail'),
	url(r'^(?P<pk>[0-9]+)/users/$', views.CentreDetailUsersListView.as_view(), name='centre-users'),
	url(r'add/$', views.CentreCreateView.as_view(), name='centre-add'),
    url(r'(?P<pk>[0-9]+)/update/$', views.CentreUpdateView.as_view(), name='centre-update'),
    url(r'(?P<pk>[0-9]+)/delete/$', views.CentreDeleteView.as_view(), name='centre-delete'),
]
