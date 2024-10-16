from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from user.models import CustomUser
from django.contrib.auth import login, logout

def signup(request):
    username = request.POST['username']
    password = request.POST['password']
    new_user = CustomUser(usrename=username, password=password)
    new_user.save()
    return HttpResponse('ユーザの作成に成功しました')

def login(request):
    username = request.POST['username']
    password = request.POST['password']

    try:
        user = CustomUser.object.get(username=username)
    except CustomUser.DoesNotExist:
        return HttpResponse('ログインに失敗しました')
    
    if user.password == password:
        login(request, user)
        return HttpResponseRedirect('/')
    else:
        return HttpResponse('ログインに失敗しました')
    
def signout(request):
    logout(request)
    return HttpResponseRedirect('/')    