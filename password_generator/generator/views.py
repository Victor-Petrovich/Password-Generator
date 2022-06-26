from django.shortcuts import render

import random


def home(request):
    return render(request, 'generator/home.html')


def about(request):
    return render(request, 'generator/about.html')


def password(request):
    characters = list('abcdefghijklmopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+='))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    lenght = int(request.GET.get('length', 12))

    thepassword = ''
    for x in range(lenght):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})
