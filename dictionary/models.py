from django.db import models
from django.conf import settings

class Dialect(models.Model):
	dialect = models.CharField(max_length=50)
	word = models.CharField(max_length=50)
	meaning = models.TextField()

	def __str__(self):
		return "{} - {}".format(self.dialect, self.word)
