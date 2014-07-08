from django.shortcuts import render
from django.http import HttpResponse
from julyapp.models import *
# Create your views here.
def homepage (request):
    return render(request, 'index.html', locals())
def mainpage (request):
    return render(request, 'mainpage.html', locals())
def hello (request):
    return HttpResponse ("Hello World")
def hello1 (request):
    return HttpResponse ("Hi Saran")
def add (request):
    a=5
    b=10
    c=a+b
    return render(request, 'add.html', locals())
def name (request):
	if request.POST:
	    firstname=request.POST.get ('firstname')
	    lastname=request.POST.get ('lastname')
	    email=request.POST.get ('email')
	    name=firstname+lastname
	    a=Contact (first_name=firstname, last_name=lastname, email1=email)
	    a.save()
	b=Contact.objects.all()
	    #name=str(firstname)+str(lastname)
	return render(request, 'name.html', locals())
    