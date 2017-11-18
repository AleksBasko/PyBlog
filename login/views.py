from django.shortcuts import render, redirect
from django.contrib import auth

def authLogin(request):
    if request.method == 'POST':
        getName = request.POST['name']
        getPassword = request.POST['password']
        user = auth.authenticate(username=getName, password=getPassword)
        if user is not None:
            auth.login(request, user)
            return redirect('/')


