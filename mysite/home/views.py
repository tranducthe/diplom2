from django.shortcuts import render
from django.http import HttpResponse
from .models import ListUni
from  django.views import View
# Create your views here.



def home_view(request):

    object_list = ListUni.objects.all()
    return  render(request,"home.html", {'object_list': object_list})

def home_detail(request,id):

    listdetail = ListUni.objects.get(id=id)
    return  render(request,"recom2.html", {'listdetail':listdetail})





def about_view(request):
    return render(request, 'about.html')

