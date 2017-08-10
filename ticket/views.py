from django.http import HttpResponse
from ticket.models import Task
from django.shortcuts import render

def home(request):
    return HttpResponse("Hello world!")

def ticket_listing(request):
    objets = Task.objects.all().order_by('-due_date')