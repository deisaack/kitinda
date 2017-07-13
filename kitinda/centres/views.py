from __future__ import unicode_literals
from django.views.generic import DetailView, DeleteView, UpdateView, TemplateView, ListView, CreateView
from django.core.urlresolvers import reverse_lazy
from .models import Centre
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.conf import settings
from django.contrib.auth.models import User

# User = settings.AUTH_USER_MODEL

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


class CentreDetailUsersListView(DetailView):
	model = Centre
	template_name = 'centres/center_users.html'


	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super(CentreDetailUsersListView, self).get_context_data(**kwargs)
		# Add in a QuerySet of all the books
		context['user_list'] = User.objects.filter(profile__centre__name='Kaborom')
		# context['test_users'] = User.objects.filter(profile__centre__name=request.user)
		# context['test_users'] = User.objects.filter(profile__centre__name=object)
		return context

class CentreDetailProductionView(DetailView):
	model = Centre

class CentreDetailPaymentView(DetailView):
	model = Centre

class CentreDetailUsersView(DetailView):
	model = Centre


class CentreList(ListView):
	model = Centre
	context_object_name = 'centre_list'
	template_name = 'centres/center_list.html'
