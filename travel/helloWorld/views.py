from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request):
    return render (request,'hello.html')

def hii(request):
    return HttpResponse('Hii World')
