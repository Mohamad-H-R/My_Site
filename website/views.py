from django.shortcuts import render

from django.http import HttpResponse


def home_view(request):
    return render(request, 'home/index.html')

def about_view(request):
    return render(request,'about.html')

def contact_view(request):
    return render(request,'contact.html') 

def test_view(request):
    return render(request, 'test.html')

