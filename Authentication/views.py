from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def loginPage(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        pwd=request.POST.get('password')
        user = authenticate(request, username=name,password=pwd) 
        if user is not None:
            login(request,user)
            return redirect('employee.profile')
        else:
            messages.error(request, 'Email or Password is Invalid!')        

    return render(request,"Authentication/login.html")

def registrationPage(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        pwd=request.POST.get('password')
        conf_pwd=request.POST.get('confirm_password')
        if pwd == conf_pwd:
            if User.objects.filter(username = name).exists():
                messages.error(request, 'Username Already Exists!')
            elif User.objects.filter(email = email).exists():
                messages.error(request, 'Email Already Exists!')   
            else:
                user= User.objects.create_user(username = name,password = pwd,email = email)    
                user.save()   
                return redirect('login')
        else:
            messages.error(request, 'password & confirm-password not matched!') 
    return render(request,"Authentication/registration.html")

def forgotpassword(request):
    return render(request,"Authentication/forgot.html")

def userlogout(request):
    logout(request)
    messages.success(request, 'Successfully Logout!')   
    return redirect('login')
