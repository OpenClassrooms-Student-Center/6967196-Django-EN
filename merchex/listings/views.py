from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from listings.models import Band, Listing
from listings.forms import BandForm, ContactUsForm, ListingForm


def band_list(request):
    bands = Band.objects.all()
    return render(request,
                  'listings/band_list.html',
                  {'bands': bands})


def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request,
                  'listings/band_detail.html',
                  {'band': band})


def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            # create a new `Band` and save it to the db
            band = form.save()
            # redirect to the detail page of the band we just created
            return HttpResponseRedirect(reverse('band-detail', kwargs={'id': band.id}))
    else:
        form = BandForm()

    return render(request,
                  'listings/band_create.html',
                  {'form': form})


def band_update(request, id):
    return render(request, 'listings/band_update.html')


def listing_list(request):
    listings = Listing.objects.all()
    return render(request,
                  'listings/listing_list.html',
                  {'listings': listings})


def listing_detail(request, id):
    listing = Listing.objects.get(id=id)
    return render(request,
                  'listings/listing_detail.html',
                  {'listing': listing})


def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/listings/')
    else:
        form = ListingForm()

    return render(request,
                  'listings/listing_create.html',
                  {'form': form})


def about(request):
    return render(request, 'listings/about.html')


def contact(request):
    if request.method == 'POST':
        # create an instance of our form, and fill it with the POST data
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonymous"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
            return HttpResponseRedirect('/email-sent/')
        # if the form is not valid, we let execution continue to the return
        # statement below, and display the form again (with errors).

    else:
        # this must be a GET request, so create an empty form
        form = ContactUsForm()

    return render(request,
                  'listings/contact.html',
                  {'form': form})

def email_sent(request):
    return render(request, 'listings/email_sent.html')
