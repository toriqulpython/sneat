from django.http import HttpResponse
from django.shortcuts import render
def homePage(request):
    return render(request, "index.html")
def login(request):
    return render(request, "auth-login-basic.html")
def register(request):
    return render(request, "auth-register-basic.html")
def password(request):
    return render(request, "auth-forgot-password-basic.html")