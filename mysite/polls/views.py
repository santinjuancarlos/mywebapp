from django.shortcuts import render
from django.http import HttpResponse
import datetime


def index(request):
    return HttpResponse("Hola mundo")

def hola_dos(request):
    return HttpResponse(str(datetime))

# Create your views here.
