from django.http import HttpResponse
from django.shortcuts import render


def startpage(request):
    return HttpResponse("You are on the startpage")
