from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from Todo.models import TODO 
from django.views.decorators.csrf import csrf_protect
@csrf_protect
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('psw')
        print(username,password)
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('/list')
    return render(request,'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('psw')
        print(username,password)
        user = authenticate(request,username=username,password=password)
        if user:
            return redirect('/login')
    if request.method == 'POST':
        username = request.POST.get('username') # this is name attributes of the input
        email = request.POST.get('email')
        password = request.POST.get('psw')
        print(username,email,password)
        new_user = User.objects.create_user(username,email,password)
        new_user.save()

        return redirect('/login')
    return render(request,'signup.html')
@csrf_protect
def listt(request):
    return render(request,'list.html')