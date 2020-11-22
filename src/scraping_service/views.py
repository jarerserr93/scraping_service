from django.shortcuts import render
import datetime


def home(requests):
    date = datetime.datetime.now().date()
    name = 'Dave'
    _context = {'date': date, 'name': name}
    return render(requests, 'home.html', _context)
