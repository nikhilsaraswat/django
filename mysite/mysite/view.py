# This file has been created by me. - Nikhil
# HttpResponse required by browser
from django.http import HttpResponse # to send text as response
from django.shortcuts import render # to send http as response

#Default argument request is required
def index(request):
    params = {'name':'harry','place':'Mars'} # parameters to parse
    return render(request, 'index.html',params) # 3 arguments first default requests, second template, 3 parameters to parse
    # return HttpResponse("hello") # Can pass text, html as inline

def analyze(request):
    djtext = request.POST.get('text','default') # get request from form in index.html first value you wants to get and second default in case no value is passed.
    # Checking checkbox values
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    newlineremover = request.POST.get('newlineremover','off')
    charcount = request.POST.get('charcount','off')
    print(removepunc)
    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if (fullcaps == "on"):
        analyzed = djtext.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        # Analyze the text
        djtext = analyzed

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed Extra spaces', 'analyzed_text': analyzed}
        # Analyze the text
        djtext = analyzed
    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        djtext = analyzed
    if(charcount == 'on'):
        analyzed = ""
        i = 0
        for char in djtext:
            if char in 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                i += 1
            analyzed = analyzed + char
        params = {'purpose':f'Count Characters {i}','analyzed_text': analyzed}
    if (removepunc == 'off' and fullcaps == 'off' and extraspaceremover == 'off' and newlineremover == "off" and charcount == 'off'):
        return HttpResponse("Error") # Can pass text, html as inline
    return render(request, 'analyze.html', params) # Can pass html file
