import csv, io
from django.core.paginator import Paginator
from copy import deepcopy
from django.core.signing import Signer
from django.shortcuts import render, redirect
from django.db import models
from django.http import HttpResponse
from django.db.models import Q
from .models import *
from .forms import *

def dictionary(request):
	return render(request,'classifier/dictionary.html')

def impcsv(request):
	template = "classifier/import.html"

	prompt = {
		'order':'Order of the CSV should be dialect, word, meaning'
	}

	if request.method == "GET":
		return render(request, template, prompt)

	csv_file = request.FILES['file']

	if not csv_file.name.endswith('.csv'):
		messages.error(request, 'This is not a csv file')

	data_set = csv_file.read().decode('UTF-8')
	io_string = io.StringIO(data_set)
	next(io_string)

	entries = Dialect.objects.all()

	for column in csv.reader(io_string, delimiter=','):
		signed_val=Signer(salt=column[0]).sign(column[2]),
		acs=deepcopy(signed_val[0].split(":")[1],)

		_, created = Dialect.objects.update_or_create(
			dialect=column[0],
			word=column[1],
			meaning=column[2]
		)

	context = {}
	return render(request, template, context)

def search_form(request):
   return render(request, 'dictionary/dictionary.html')

def search(request):
	error = False

	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			error = True
		else:
			posts = Dialect.objects.filter( Q(word__icontains=q))
			return render(request, 'classifier/search_result.html', {'posts':posts, 'query':q})
	return render(request, 'classifier/dictionary.html', {'error': error})

def waray_dictionary(request):
	waray_list = Dialect.objects.filter(dialect='Waray')
	paginator = Paginator(waray_list, 20)
	page = request.GET.get('page')
	posts = paginator.get_page(page)

	return render(request, 'classifier/waray_dictionary.html', {'posts': posts} )

def cebuano_dictionary(request):
	cebuano_list = Dialect.objects.filter(dialect='Cebuano')
	paginator = Paginator(cebuano_list, 20)
	page = request.GET.get('page')
	posts = paginator.get_page(page)

	return render(request, 'classifier/cebuano_dictionary.html', {'posts': posts} )

def hiligaynon_dictionary(request):
	hiligaynon_list = Dialect.objects.filter(dialect='Hiligaynon')
	paginator = Paginator(hiligaynon_list, 20)
	page = request.GET.get('page')
	posts = paginator.get_page(page)

	return render(request, 'classifier/hiligaynon_dictionary.html', {'posts': posts} )

