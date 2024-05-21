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

    # list_filter = [
    #     'campos_fk_e_booleanos
    # ]

    # list_select_related = [
    #     'campos_dos_campos_fk
    # ]

    # autocomplete_fields = [
    #     'campos_fk
    # ]
