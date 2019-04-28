from django.shortcuts import render, redirect
from .models import InputDialect
from .forms import InputForm


def base(request):
	form = InputForm()
	if request.method == "POST":
		form = InputForm(data=request.POST)
		if form.is_valid():
			form = form.save(commit=False)
			form.save()
			return HttpResponseRedirect(reverse('index'))
		else:
			return render(request,'classifier/index.html', {"form": form})


def home(request):
    return render(request,'classifier/home.html')

def dictionary(request):
    return render(request,'classifier/dictionary.html')