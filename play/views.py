from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def play(request):
    return HttpResponse('Smooth life')