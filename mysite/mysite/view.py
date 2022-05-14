# This file has been created by me. - Nikhil
from django.http import HttpResponse
def index(request):
    return HttpResponse("hello")

def about(request):
    return HttpResponse("about us")
