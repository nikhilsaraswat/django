# This file has been created by me. - Nikhil
# HttpResponse required by browser
from django.http import HttpResponse
from django.shortcuts import render
#Default argument request is required
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("hello") # Can pass text, html

def removepunc(request):
    return HttpResponse("remove punc")

def capfirst(request):
    return HttpResponse("capitalize first")

def newlineremove(request):
    return HttpResponse("about us")

def spaceremove(request):
    return HttpResponse("new line remove <a href='/'>back</a>")

def charcount(request):
    return HttpResponse("char count")
