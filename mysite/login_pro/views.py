from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.views.generic import TemplateView
from .form import RegisterationForm, loginForm
from django.http import HttpResponseRedirect, HttpResponse
from django.views import View
from django.contrib.auth.models import User
# Create your views here.


class register(View):
    def get(self,request):
        rf = RegisterationForm()
        return render(request,'register.html',{'rf': rf})
    def post(self,request):
        username= request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(username,email,password)
        user.save()
        return HttpResponse('save user success')

class loginUser(View):
    def get(self,request):
        lf=loginForm
        return render(request,'login.html',{'lf':lf})
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('Login success')
        else:
            return HttpResponse('Login fail')

def logoutUser(request):
    logout(request)
    return HttpResponse('you are logout')
