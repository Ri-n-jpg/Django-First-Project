from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremove= request.GET.get('newlineremove','off')
    extraspaceremove= request.GET.get('extraspaceremove',"off")

    if removepunc == "on":
        analyzed = ""
        punctuations = "!()-[]{};:'\"\\<>?.,_"

        for char in djtext:
            if char not in punctuations:
                analyzed += char

        params = {
            'purpose': 'Removed Punctuations',
            'analyzed_text': analyzed
        }

        return render(request, 'analyzed.html', params)

    elif fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()

        params = {
            'purpose': 'Change to UpperCase',
            'analyzed_text': analyzed
        }

        return render(request, 'analyzed.html', params)
    elif(newlineremove == "on"):
        analyzed = ""
        for char in djtext:
            if char!="\n":
             analyzed += char

        params = {
            'purpose': 'Removed NewLines',
            'analyzed_text': analyzed
        }
        return render(request, 'analyzed.html',params)
    elif extraspaceremove == "on":
        analyzed = ""

        for index, char in enumerate(djtext):
            if index < len(djtext) - 1:
                if not (djtext[index] == " " and djtext[index + 1] == " "):
                    analyzed += char
            else:
                analyzed += char

        params = {
            'purpose': 'Removed Extra Spaces',
            'analyzed_text': analyzed
        }

        return render(request, 'analyzed.html', params)
    else:
        return HttpResponse("Error")


def capitalizefirst(request):
    return HttpResponse("capitalize")


def newlineremove(request):
    return HttpResponse("newlineremove")


def spaceremove(request):
    return HttpResponse("space remove <a href='/home/'>back</a>")


def charcount(request):
    return HttpResponse("char count")