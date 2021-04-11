from django.contrib import admin

from listings.models import Band, Listing


class BandAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ListingAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Band, BandAdmin)
admin.site.register(Listing, ListingAdmin)
