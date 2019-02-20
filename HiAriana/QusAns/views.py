from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("Ready to start app")
