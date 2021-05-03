from django.shortcuts import render
from django.http import HttpResponse
from .models import recom
# Create your views here.

def recom1(request,id):
    rc = recom.objects.get(id=id)
    return render(request, 'recom1.html', {'rc':rc})

