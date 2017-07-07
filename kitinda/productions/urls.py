from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^new/$', views.new, name='new_supply'),
	url(r'^$', views.SupplyList.as_view(), name='supply-list'),
	url(r'^(?P<pk>[0-9]+)/$', views.SupplyDetailView.as_view(), name='supply-detail'),
	url(r'^add/$', views.SupplyCreateView.as_view(), name='supply-add'),
	url(r'^(?P<pk>[0-9]+)/update/$', views.SupplyUpdateView.as_view(), name='supply-update'),
	url(r'^(?P<pk>[0-9]+)/delete/$', views.SupplyDeleteView.as_view(), name='supply-delete'),
	url(r'^receive/$', views.supply_receive, name='receive'),
	url(r'^users/$', views.users, name='users_message'),
	url(r'^new/$', views.new, name='new_supply'),
]
