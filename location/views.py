from django.shortcuts import render

from django.http import HttpResponse



def destinations(request):
    return render(request,'destinations.html')