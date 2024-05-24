from django.contrib import admin

from ..models import Withdraw


@admin.register(Withdraw)
class WithdrawAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'investment'
    ]

    search_fields = [
        'id',
        
    ]

    autocomplete_fields = [
        'investment'
    ]
