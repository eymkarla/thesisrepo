import csv, io
from copy import deepcopy
from django.core.signing import Signer
from django.shortcuts import render, redirect
from django.db import models
from django.http import HttpResponse
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

def samples(request):
	test = 'Kunta tigbas harayu Pangit test test2'
	test_lower = test.lower()
	user_inputs = test_lower.split(' ')
	warays = Language.objects.filter(dialect='Waray')
	cebus = Language.objects.filter(dialect='Cebuano')
	waray_count = 0
	cebu_count = 0

	for waray in warays:
		for user_input in user_inputs:
			if waray.word == user_input:
				waray_count += 1
	
	for cebu in cebus:
		for user_input in user_inputs:
			if cebu.word == user_input:
				cebu_count += 1
				
	return render(request,'classifier/samples.html')