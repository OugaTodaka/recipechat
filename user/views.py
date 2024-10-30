from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from user.models import CustomUser
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import check_password,make_password

def signin(request):
    template = loader.get_template("user/signin.html")
    return HttpResponse(template.render(None, request))

def signup(request):
    template = loader.get_template("user/signup.html")
    return HttpResponse(template.render(None, request))


def signup_sys(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
        pass_word = make_password(password)
        new_user = CustomUser(username=username, password=pass_word)
        new_user.save()
        login(request, new_user)
        return HttpResponseRedirect('/')
    except:
        return HttpResponse('ユーザ作成に失敗しました')

def signin_sys(request):
    username = request.POST['username']
    password = request.POST['password']

    try:
        user = CustomUser.objects.get(username=username)
    except CustomUser.DoesNotExist:
        return HttpResponse('ログインに失敗しました')
    
    if check_password(password, user.password):
        login(request, user)
        return HttpResponseRedirect("/")
    else:
        return HttpResponse('ログインに失敗しました')
    
def signout_sys(request):
    logout(request)
    return HttpResponseRedirect('/user/signin')