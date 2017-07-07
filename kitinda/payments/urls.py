from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.PaymentList.as_view(), name='payment-list'),
	url(r'^(?P<pk>[0-9]+)/$', views.PaymentDetailView.as_view(), name='payment-detail'),
	url(r'add/$', views.PaymentCreateView.as_view(), name='payment-add'),
	url(r'(?P<pk>[0-9]+)/update/$', views.PaymentUpdateView.as_view(), name='payment-update'),
	url(r'(?P<pk>[0-9]+)/delete/$', views.PaymentDeleteView.as_view(), name='payment-delete'),
]
