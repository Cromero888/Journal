from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from . models import Strain, Strain_validator

# def home(request, id):
# 	context = {
# 		'stuff': Home.objects.get(id=id)
# 	}
# 	return render(request, 'home.html', context),

def index(request):
    return render(request, "home.html")

def journal(request):
    context = {
        'strain': Strain.objects.all()
    }
    return render(request, "journal.html", context)

def addstrain(request):
    errors = Strain.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')


    else:
        strain = Strain.objects.create(
            strain_name = request.POST['strain_name'],
            grower = request.POST['grower'],
            dispensary = request.POST['dispensary'],
            cannabis = request.POST['cannabis'],
            medium = request.POST['medium'],
            price = request.POST['price'],
            rating = request.POST['rating'],
            amount = request.POST['amount']
        )
        strain.save()
        return redirect('/')
