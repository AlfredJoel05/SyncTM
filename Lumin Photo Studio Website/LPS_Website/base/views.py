from django.shortcuts import render
from django.http import HttpResponse

def home(response):
    return HttpResponse('Home Page')
def about(response):
    return HttpResponse('About Page')