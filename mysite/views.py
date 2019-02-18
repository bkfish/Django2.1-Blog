from django.contrib import auth
from django.shortcuts import render_to_response, redirect, render
from django.urls import reverse

def home(request):
    context = {}
    return render_to_response('home.html', context)


def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(request, username=username, password=password)
    referer=request.META.get('HTTP_REFERER',reverse('home'))
    if user is not None:
        auth.login(request, user)
        return redirect(referer)
    else:
        return render(request, 'error.html', {'message': '用户名密码不正确'})


def logout(request):
    referer = request.META.get('HTTP_REFERER', reverse('home'))
    if request.method == 'POST':
        auth.logout(request)
        return redirect(referer)
