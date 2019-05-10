from copy import deepcopy
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.urls import reverse
from django.http import HttpResponseRedirect, Http404
from .models import InputDialect
from .forms import InputForm
from classifier.NB import NaiveBayes


class ClassifyView(TemplateView):
	template_name = "classifier/classify.html"

	def get(self, request):
		form = InputForm()
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = InputForm(request.POST)
		if form.is_valid():
			text = form.cleaned_data['text_input']

		args = {'form':form, 'text': text}
		# return render(request, self.template_name, args)
		return HttpResponseRedirect('/classifier_result/%s' % (text))

	
class ResultView(TemplateView):
	template_name = "classifier/classifier_result.html"

	def get(self, request, *args, **kwargs):
		text_input = deepcopy(kwargs['text_input'])
		form = InputForm(initial={'text_input':text_input})
		naive1 = NaiveBayes.train(text_input)
		print(naive1)

		return render(request, self.template_name, {'form': form, 'display_input': text_input}, )


def home(request):
	 return render(request,'classifier/home.html')

def dictionary(request):
	 return render(request,'classifier/dictionary.html')

def sam(request):
	 return render(request,'classifier/s.html')