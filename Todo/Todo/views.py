from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from Todo.models import TODO 
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('listt')
    return render(request,'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('psw')
        print(username,password,email)
        user = authenticate(request,username=username,password=password)
        if user is None:
            new_user = User.objects.create_user(username,email,password)
            new_user.save()
        return redirect('login')
    return render(request,'signup.html')
@login_required(login_url='/login')
def listt(request):
    return render(request,'list.html')