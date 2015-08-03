from django.shortcuts import render
from django.http import HttpResponse
from entries.models import Client, Project, Entry

# Create your views here.


def clients(request):

    clients = Client.objects.all()
    return render(request, 'template.html', {'category': 'Clients', 'object_list': clients})


def projects(request):

    projects = Project.objects.all()
    return render(request, 'template.html', {'category': 'Projects', 'object_list': projects})


def getEntries(client):

    summary = Entry.objects.order_by('project').filter(project__client__name=client)
    return summary


def clientsummary(request):

    clients = Client.objects.all()
    results = {}
    for client in clients:
        results[client.name] = getEntries(client.name)

    return render(request, 'clientsummary.html', {'category': 'Client Summary', 'object_list': results})
