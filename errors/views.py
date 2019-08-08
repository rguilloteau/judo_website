from django.shortcuts import render
from django.http import HttpResponse


def error404(request, exception):
    return render(request,'errors/404.html')