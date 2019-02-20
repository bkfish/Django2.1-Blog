from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, redirect, render
from django.urls import reverse
from .forms import LoginForm, RegForm


def home(request):
    context = {}
    return render_to_response('home.html', context)


def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            auth.login(request, user)
            return redirect(request.GET.get('from', reverse('home')))

    else:
        login_form = LoginForm()

    context = {}
    context['login_form'] = login_form
    return render(request, 'login.html', context)


def logout(request):
    referer = request.META.get('HTTP_REFERER', reverse('home'))
    if request.method == 'POST':
        auth.logout(request)
        return redirect(referer)


def register(request):
    if request.method == 'POST':
        reg_form = RegForm(request.POST)
        if reg_form.is_valid():
            username = reg_form.cleaned_data['username']
            email = reg_form.cleaned_data['email']
            password = reg_form.cleaned_data['password']
            # 创建用户
            user = User.objects.create_user(username, email, password)
            user.save()
            # 登录用户
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return redirect(request.GET.get('from', reverse('home')))
    else:
        reg_form = RegForm()

    context = {}
    context['reg_form'] = reg_form
    return render(request, 'register.html', context)
