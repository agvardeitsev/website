from django.http import HttpResponse
from django.shortcuts import render

def General(request):
    return  render (request,'webfilling/general.html')
def Gvardeitsev(request):
    return  render (request,'webfilling/gvard.html')
def Denis(request):
    return  render (request,'webfilling/denis.html')
def Tanya(request):
    return  render (request,'webfilling/tanya.html')
def Maxus(request):
    return  render (request,'webfilling/maxus.html')
def Vital(request):
    return  render (request,'webfilling/vital.html')
def Alex(request):
    return  render (request,'webfilling/alex.html')
def Lugas(request):
    return  render (request,'webfilling/lugas.html')

