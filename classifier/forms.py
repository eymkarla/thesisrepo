from django import forms
from django.forms import ModelForm
from django.conf import settings
from .models import InputDialect

class InputForm(forms.ModelForm):
	class Meta:
		model = InputDialect
		fields = ['text_input']