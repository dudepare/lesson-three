from django.shortcuts import render
from django.http import HttpResponse
from entries.models import Client, Project

# Create your views here.
def clients(request):
	clients = Client.objects.all()
	return render(request, 'template.html', {'category': 'Clients', 'object_list': clients})

def projects(request):
	projects = Project.objects.all()
	return render(request, 'template.html', {'category': 'Projects', 'object_list': projects})

def clientsummary(request):
	return render(request, 'template.html', {'category': 'Client Summary'})