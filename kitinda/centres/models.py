from django.db import models
from geoposition.fields import GeopositionField
from django.core.urlresolvers import reverse



class Centre(models.Model):
	name = models.CharField(max_length=30, unique=True)
	description = models.TextField(max_length=500, null=True, blank=True)
	location = GeopositionField()

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('centre:centre-detail', kwargs={'pk': self.pk})

