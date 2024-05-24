from django.contrib import admin

from ..models import Investor


@admin.register(Investor)
class InvestorAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'user',
        'name'
    ]

    search_fields = [
        'id',
        'name'
    ]

    autocomplete_fields = [
        'user'
    ]
