from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from . import views as SiteLoginView_pro
app_name ='UserMember'

urlpatterns = [


    path('register/',views.register.as_view(), name="register"),
    path('loginUser/',views.loginUser.as_view(), name="loginUser"),
    path('logoutUser/', views.logoutUser, name="logoutUser"),
]