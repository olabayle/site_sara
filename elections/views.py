from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    """Page principale du site de Sara!!!"""
    return render(request, 'elections/elections.html' ,locals())