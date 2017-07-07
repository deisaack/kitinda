from __future__ import unicode_literals
from django.views.generic import DetailView, DeleteView, UpdateView, TemplateView, ListView, CreateView
from django.core.urlresolvers import reverse_lazy
from .models import Rank, Employee
from django.urls import reverse_lazy


class EmployeeCreateView(CreateView):
	model = Employee
	fields = ['employee_id', 'user', 'centre', 'rank', 'description']
	template_name = 'employees/new_employee.html'

class EmployeeUpdateView(UpdateView):
	model = Employee
	fields = ['employee_id', 'user', 'centre', 'rank', 'description']
	template_name = 'employees/new_employee.html'

class EmployeeDeleteView(DeleteView):
	model = Employee
	success_url = reverse_lazy('employee/employee-list')

class EmployeeDetailView(DetailView):
	model = Employee


class EmployeeList(ListView):
	model = Employee
	context_object_name = 'employee_list'
	template_name = 'employees/employee_list.html'



class RankCreateView(CreateView):
	model = Rank
	fields = ['name', 'description']
	template_name = 'employees/new_rank.html'

class RankUpdateView(UpdateView):
	model = Rank
	fields = ['name', 'description']
	template_name = 'employees/new_rank.html'

class RankDeleteView(DeleteView):
	model = Rank
	success_url = reverse_lazy('employee/rank-list')

class RankDetailView(DetailView):
	model = Rank


class RankList(ListView):
	model = Rank
	context_object_name = 'rank_list'
	template_name = 'employees/rank_list.html'

