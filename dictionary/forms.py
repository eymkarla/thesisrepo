from django import forms
from django.forms import ModelForm
from .models import Dialect
from django.conf import settings

class DialectForm(forms.ModelForm):
	class Meta:
		model = Dialect
		fields = ['dialect','word','meaning']