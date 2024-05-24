from django.contrib import admin

from ..models import Investiment


@admin.register(Investiment)
class InvestimentAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'owner',
        'creation_date',
        'value'
    ]

    search_fields = [
        'id',
        
    ]

    autocomplete_fields = [
        'owner'
    ]
