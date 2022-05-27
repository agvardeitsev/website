from django.http import HttpResponse
from django.shortcuts import render

def general(request):
    return  render (request,'general.html')