from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm,LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#首頁
@login_required(login_url="error.html")
def index(request):
    return render(request, 'accounts/login.html')
#註冊
def sign_up(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  #重新導向到登入畫面
    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context)

#登入
def sign_in(request):
    form = LoginForm()
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('expenses/')  #重新導向到首頁
        else:
            return render(request,'accounts/error.html')
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

# 登出
def log_out(request):
    logout(request)
    return redirect('/') #重新導向到登入畫面