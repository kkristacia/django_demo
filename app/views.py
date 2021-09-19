from django.shortcuts import render
from django.db import connections

from app.utils import namedtuplefetchall


def index(request):
    context = {'nbar': 'home'}
    return render(request, 'index.html', context)


def db(request):
    with connections['default'].cursor() as cursor:
        cursor.execute('INSERT INTO app_greeting ("when") VALUES (NOW());')
        cursor.execute('SELECT "when" FROM app_greeting;')
        greetings = namedtuplefetchall(cursor)

    context = {'greetings': greetings, 'nbar': 'db'}
    return render(request, 'db.html', context)


def tpc_c(request):
    context = {'nbar': 'tpc-c'}
    return render(request, 'tpc-c.html', context)


def project(request):
    context = {'nbar': 'project'}
    return render(request, 'project.html', context)