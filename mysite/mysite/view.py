# This file has been created by me. - Nikhil
# HttpResponse required by browser
from django.http import HttpResponse
#Default argument request is required
def index(request):
    return HttpResponse("hello") # Can pass text, html

def about(request):
    return HttpResponse("about us")
