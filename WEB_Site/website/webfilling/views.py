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


