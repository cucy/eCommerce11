from django.contrib.auth import get_user_model, login, authenticate
from django.shortcuts import render, redirect

from .forms import LoginForm, RegisterForm


def login_page(request):
    """登录页"""
    form = LoginForm(request.POST or None)
    context = {"form": form}
    print("用户登录")
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            print(request.user.is_authenticated())
            login(request, user)
            return redirect("/")
        else:
            print("Error")
    return render(request, 'accounts/login.html', context)


User = get_user_model()


def register_page(request):
    """注册页面"""
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        print(new_user)

    return render(request, "accounts/register.html", context)
