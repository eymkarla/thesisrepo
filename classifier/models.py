from django.db import models
from django.conf import settings

class InputDialect(models.Model):
	text_input = models.TextField()

	def __str__(self):
		return f"{self.text_input}"