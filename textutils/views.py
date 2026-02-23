from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.POST.get('text', '')

    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    extraspaceremove = request.POST.get('extraspaceremove', 'off')

    analyzed = djtext   # ✅ initialize once

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        temp = ""
        for char in analyzed:
            if char not in punctuations:
                temp += char
        analyzed = temp

    if fullcaps == "on":
        temp = ""
        for char in analyzed:
            temp += char.upper()
        analyzed = temp

    if newlineremove == "on":
        temp = ""
        for char in analyzed:
            if char != "\n" and char != "\r":   # ✅ fixed
                temp += char
        analyzed = temp

    if extraspaceremove == "on":
        temp = ""
        for index, char in enumerate(analyzed):
            if not (char == " " and index + 1 < len(analyzed) and analyzed[index + 1] == " "):
                temp += char
        analyzed = temp

    # ✅ handle no checkbox selected
    if not (removepunc == "on" or fullcaps == "on" or newlineremove == "on" or extraspaceremove == "on"):
        return HttpResponse("Please select at least one operation")

    params = {
        'purpose': 'Text Analyzed',
        'analyzed_text': analyzed
    }

    return render(request, 'analyzed.html', params)



def capitalizefirst(request):
    return HttpResponse("capitalize")


def newlineremove(request):
    return HttpResponse("newlineremove")


def spaceremove(request):
    return HttpResponse("space remove <a href='/home/'>back</a>")


def charcount(request):
    return HttpResponse("char count")