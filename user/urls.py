from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'user'

urlpatterns = [
    path("signin/",
         auth_views.LoginView.as_view(template_name='user/signin.html'),
         name="signin"),
    path("signup/",views.signup,name="signup"),
    path("signin_sys/",views.signin_sys,name='signin_sys'),
    path("signup_sys/",views.signup_sys,name='signup_sys'),
    path("signout_sys/",views.signout_sys,name='signout_sys'),
]
