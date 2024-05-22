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

    # list_filter = [
    #     'campos_fk_e_booleanos
    # ]

    # list_select_related = [
    #     'campos_dos_campos_fk
    # ]

    autocomplete_fields = [
        'user'
    ]
