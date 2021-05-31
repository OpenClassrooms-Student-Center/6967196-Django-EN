from django.http import HttpResponse
from django.shortcuts import render

from listings.models import Band, Listing


def band_list(request):
    bands = Band.objects.all()
    return render(request,
                  'listings/band_list.html',
                  {'bands': bands})


def about(request):
    return render(request, 'listings/about.html')


def listings(request):
    listings = Listing.objects.all()
    return render(request,
                  'listings/listings.html',
                  {'listings': listings})


def contact(request):
    return render(request, 'listings/contact.html')
