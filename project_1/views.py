from django.shortcuts import render
from django.http import HttpResponse

def home(request) :
    return HttpResponse("This is first app page")
def courses(request) :
    return HttpResponse("THis is first app/ page")
def about(request):
    return HttpResponse("THis is first app/ about page ...")
