from __future__ import unicode_literals
from django.views.generic import DetailView, DeleteView, UpdateView, TemplateView, ListView, CreateView
from django.core.urlresolvers import reverse_lazy
from .models import Payment
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class PaymentCreateView(CreateView):
	model = Payment
	fields = ['user', 'description', 'amount', 'debit']
	template_name = 'payments/new_payment.html'

class PaymentUpdateView(UpdateView):
	model = Payment
	fields = ['user', 'description', 'amount', 'debit']
	template_name = 'payments/new_payment.html'

class PaymentDeleteView(DeleteView):
	model = Payment
	success_url = reverse_lazy('payment/payment-list')

class PaymentDetailView(DetailView):
	model = Payment


class PaymentList(ListView):
	model = Payment
	context_object_name = 'payment_list'
	template_name = 'payments/payment_list.html'
