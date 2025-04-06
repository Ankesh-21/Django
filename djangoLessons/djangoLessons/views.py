from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    # return HttpResponse('Hello World!!')
    return render(request,'websites/index.html')

def About(request):
   return render(request,'websites/about.html')

def Contact(request):
    # return HttpResponse('Hello From Contact Section')
    return render(request,'websites/contact.html')
