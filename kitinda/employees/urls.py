from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.EmployeeList.as_view(), name='employee-list'),
	url(r'^(?P<pk>[0-9]+)/$', views.EmployeeDetailView.as_view(), name='employee-detail'),
	url(r'^add/$', views.EmployeeCreateView.as_view(), name='employee-add'),
	url(r'^(?P<pk>[0-9]+)/update/$', views.EmployeeUpdateView.as_view(), name='employee-update'),
	url(r'^(?P<pk>[0-9]+)/delete/$', views.EmployeeDeleteView.as_view(), name='employee-delete'),

	url(r'^rank/$', views.RankList.as_view(), name='rank-list'),
	url(r'^rank/(?P<pk>[0-9]+)/$', views.RankDetailView.as_view(), name='rank-detail'),
	url(r'^rank/add/$', views.RankCreateView.as_view(), name='rank-add'),
	url(r'^rank/(?P<pk>[0-9]+)/update/$', views.RankUpdateView.as_view(), name='rank-update'),
	url(r'^rank/(?P<pk>[0-9]+)/delete/$', views.RankDeleteView.as_view(), name='rank-delete'),
]
