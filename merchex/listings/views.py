from django.http import HttpResponse
from django.shortcuts import render

from listings.models import Band, Listing


def hello(request):
    bands = Band.objects.all()
    return render(request,
                  'listings/hello.html',
                  {'bands': bands})


def about(request):
    return HttpResponse('<h1>About Us</h1> <p>We love merch!</p>')


def listings(request):
    listings = Listing.objects.all()
    return HttpResponse(f"""
        <h1>Listings</h1>
        <p>Check out the latest listings below!</p>
        <ul>
            <li>{listings[0].title}</li>
            <li>{listings[1].title}</li>
            <li>{listings[2].title}</li>
            <li>{listings[3].title}</li>
        </ul>
    """)


def contact(request):
    return HttpResponse('<h1>Contact Us</h1> <p>We\'re here to help.<p>')
