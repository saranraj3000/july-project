from django.shortcuts import render, HttpResponseRedirect
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

def edit (request,id):
	b=Contact.objects.get(id=id)
	if request.POST:
		b.first_name=request.POST.get ('firstname')
		b.last_name=request.POST.get ('lastname')
		b.email1=request.POST.get ('email')
		b.save()
		return HttpResponseRedirect('/list')
	return render(request, 'edit.html', locals())

def list (request):
	b=Contact.objects.all()
	return render(request, 'list.html', locals())

def delete (request,id):
	b=Contact.objects.get(id=id)
	if request.POST:
		b.delete()
		return HttpResponseRedirect('/list')
	return render(request, 'delete.html', locals())
		#return HttpResponseRedirect('/list')
	#return render(request, 'edit.html', locals())
	#return HttpResponseRedirect('/list')