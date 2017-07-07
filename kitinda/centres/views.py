from __future__ import unicode_literals
from django.views.generic import DetailView, DeleteView, UpdateView, TemplateView, ListView, CreateView
from django.core.urlresolvers import reverse_lazy
from .models import Centre
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class CentreCreateView(CreateView):
	model = Centre
	fields = ['name', 'description', 'location']
	template_name = 'centres/new_centre.html'

class CentreUpdateView(UpdateView):
	model = Centre
	fields = ['name', 'description', 'location']
	template_name = 'centres/new_centre.html'

class CentreDeleteView(DeleteView):
	model = Centre
	success_url = reverse_lazy('centre/centre-list')

class CentreDetailView(DetailView):
	model = Centre


class CentreList(ListView):
	model = Centre
	context_object_name = 'centre_list'
	template_name = 'centres/center_list.html'
