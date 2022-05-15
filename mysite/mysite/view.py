# This file has been created by me. - Nikhil
# HttpResponse required by browser
from django.http import HttpResponse # to send text as response
from django.shortcuts import render # to send http as response
#Default argument request is required
def index(request):
    params = {'name':'harry','place':'Mars'} # parameters to parse
    return render(request, 'index.html',params) # 3 arguments first default requests, second template, 3 parameters to parse
    # return HttpResponse("hello") # Can pass text, html as inline

def removepunc(request):
    djtext = request.GET.get('text','default') # get request from form in index.html first value you wants to get and second default in case no value is passed.
    #analyze the text

    return HttpResponse("remove punc")

def capfirst(request):
    return HttpResponse("capitalize first")

def newlineremove(request):
    return HttpResponse("about us")

def spaceremove(request):
    return HttpResponse("new line remove <a href='/'>back</a>")

def charcount(request):
    return HttpResponse("char count")
