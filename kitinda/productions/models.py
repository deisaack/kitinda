from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
from kitinda.employees.models import Employee
from django.db.models import Max

User = settings.AUTH_USER_MODEL

class Supply(models.Model):
	supplied_by = models.ForeignKey(User, related_name='+', default=1)
	quantity = models.FloatField('Quantity in litres', default=0.00)
	date = models.DateTimeField(auto_now_add=True)
	received_by = models.ForeignKey(User, related_name='+', default=1)

	def get_absolute_url(self):
		return reverse('production:supply-detail', kwargs={'pk': self.pk})


	def __str__(self):
		return str(self.quantity)

	@staticmethod
	def send_message(received_by, to_user, quantity):
		current_user_message = Supply(received_by=received_by,
		                       quantity = quantity,
		                       supplied_by=to_user,
		                       )
		current_user_message.save()


		return current_user_message

