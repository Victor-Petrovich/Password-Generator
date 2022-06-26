from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):



    characters = list('abcdefghijklmopqrstuvwxyz')

    lenght = 10

    thepassword = ''
    for x in range(lenght):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})
