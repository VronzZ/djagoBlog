import imp
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def showBlog(request):
    context = {}
    return render(request, 'index.html', context)