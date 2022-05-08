from django.shortcuts import render
from django.http import HttpResponse

def userstatistics(request):
    return HttpResponse('Статистика')
