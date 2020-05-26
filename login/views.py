from django.shortcuts import render, redirect
from .models import User
from . import models
from .forms import *
# Create your views here.


def register(request):
    if request.method == "POST":
        name = request.POST['name']
        password = request.POST['password']
        obj = User.objects.create(name = name, password = password)
        request.session['user_id'] = obj.id
        return redirect('/crtop')
    return render(request, 'register.html')


def login(request) :
    if request.method == "POST":
        login_form = user_entry(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            print("通过验证")
            username = login_form.cleaned_data['name']
            password = login_form.cleaned_data['password']
            print(username)
            print(password)
            try:
                user = User.objects.get(name=username)

                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    request.session['user_type'] = user.user_type
                    if user.user_type == 1:
                        return redirect('/admin/')
                    else :
                        return redirect('/show/')
                else :
                    message = "密码不正确!"
            except:
                message = "用户不存在！"
        return render(request, 'login.html', locals())
    login_form = user_entry()
    return render(request, 'login.html', locals())

def operate(request) :
    return render(request, 'operate.html')

def logout(request) :
    if not request.session.get('is_login', None):
        return redirect("/login/")
    request.session.flush()
    return render(request, 'login.html')