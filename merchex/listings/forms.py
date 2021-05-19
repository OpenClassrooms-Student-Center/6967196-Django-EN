from django import forms

from listings.models import Band, Listing


class ContactUsForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField()


class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        exclude = ('active', 'official_homepage')


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = '__all__'
