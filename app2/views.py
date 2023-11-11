from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
    return render(request,'second.html')
def second(request):
    return HttpResponse('<h1> This second function of second application</h1')
