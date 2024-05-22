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

    # list_filter = [
    #     'campos_fk_e_booleanos
    # ]

    # list_select_related = [
    #     'campos_dos_campos_fk
    # ]

    autocomplete_fields = [
        'investment'
    ]
