from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
from kitinda.centres.models import Centre


User = settings.AUTH_USER_MODEL


class Rank(models.Model):
	name = models.CharField(max_length=30, unique=True)
	description = models.TextField(max_length=500, null=True, blank=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('employees:rank-detail', kwargs={'pk': self.pk})

class Employee(models.Model):
	employee_id = models.CharField(max_length=20, unique=True)
	user = models.OneToOneField(User)
	centre = models.ForeignKey(Centre)
	rank = models.ForeignKey(Rank)
	description = models.CharField(max_length=250, null=True, blank=True)

	def __str__(self):
		return self.employee_id

	def get_absolute_url(self):
		return reverse('employees:employee-detail', kwargs={'pk': self.pk})
