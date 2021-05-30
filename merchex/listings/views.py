from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse('<h1>Hello Django!</h1>')


def about(request):
    return HttpResponse('<h1>About Us</h1> <p>We love merch!</p>')


def listings(request):
    return HttpResponse('<h1>Listings</h1> <p>Check out the latest listings below!</p>')


def contact(request):
    return HttpResponse('<h1>Contact Us</h1> <p>We\'re here to help.<p>')
