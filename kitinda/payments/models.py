from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings


User = settings.AUTH_USER_MODEL


class Payment(models.Model):
	user = models.ForeignKey(User)
	description = models.CharField(max_length=200)
	amount = models.FloatField(default=0.00)
	debit = models.BooleanField(default=True)

	def __str__(self):
		return self.amount

	def get_absolute_url(self):
		return reverse('payment:payment-detail', kwargs={'pk': self.pk})

