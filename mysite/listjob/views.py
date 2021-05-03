from django.shortcuts import render
from django.http import HttpResponse
from .models import ListAreas
# Create your views here.

def job_view(request):

    object_listJob = ListAreas.objects.all()
    return  render(request,"listjob.html", {
        'object_list': object_listJob
    })

def Detailjob_view(request,id):

    object_Detailjob = ListAreas.objects.get(id=id)
    return  render(request,"listjob.html", {'object_list': object_Detailjob })
