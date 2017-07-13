from django.views.generic import DetailView, DeleteView, UpdateView, TemplateView, ListView, CreateView
from django.core.urlresolvers import reverse_lazy
from .models import Supply
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .forms import SupplyForm
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from kitinda.decorators import ajax_required
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
import json
from django.urls import reverse
User = settings.AUTH_USER_MODEL
from .models import Supply



@login_required
@ajax_required
def users(request):
	users = User.objects.filter(is_active=True)
	dump = []
	template = '{0} ({1})'
	for user in users:
		if user.profile.get_screen_name() != user.username:
			dump.append(template.format(user.profile.get_screen_name(),
	                                    user.username))
		else:
			dump.append(user.username)
	data = json.dumps(dump)
	return HttpResponse(data, content_type='application/json')


class SupplyCreateView(CreateView):
	model = Supply
	fields = ['supplied_by', 'quantity']
	template_name = 'supply/new_supply.html'


class SupplyUpdateView(UpdateView):
	model = Supply
	fields = ['supplied_by', 'quantity']
	template_name = 'supply/new_supply.html'


class SupplyDeleteView(DeleteView):
	model = Supply
	success_url = reverse_lazy('supply/supply-list')


class SupplyDetailView(DetailView):
	model = Supply
	template_name = 'supply/supply_detail.html'


class SupplyList(ListView):
	model = Supply
	context_object_name = 'supply_list'
	template_name = 'supply/supply_list.html'








""" 
Testspace starts here 

"""


import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages


@login_required
def new(request):
	if request.method == 'POST':
		received_by = request.user
		quantity = request.POST.get('quantity')
		to_user_username = request.POST.get('to')
		try:
			to_user = User.objects.get(username=to_user_username)
		
		except Exception:
			try:
				to_user_username = to_user_username[
		            to_user_username.rfind('(')+1:len(to_user_username)-1]
				to_user = User.objects.get(username=to_user_username)
		
			except Exception:
				return redirect('/')

		# message = request.POST.get('message')
		obj = Supply.objects.all().count()
		obj = Supply
		if received_by != to_user:
			Supply.new_supply(received_by, to_user, quantity)
			messages.success(request, 'The supply was successfully saved.')
		return HttpResponseRedirect(reverse('production:supply-list'))

		# return redirect(obj)
		
	else:
		return render(request, 'productions/new.html')
