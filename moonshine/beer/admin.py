from django.contrib import admin

from .models import BeerModel

class BeerAdmin(admin.ModelAdmin):

    fields = [
        'name',
        'beer_type',
        'description',
        ]


admin.site.register(BeerModel, BeerAdmin)
