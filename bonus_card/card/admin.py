from django.contrib import admin

from card.models import Applying, Card


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('series', 'number', 'release_date', 'end_date', 'card_status')
    list_editable = ('card_status',)
    search_fields = ('card_status',)
    list_filter = ('number',)
    empty_value_display = '-пусто-'


@admin.register(Applying)
class ApplyingAdmin(admin.ModelAdmin):
    list_display = ('card', 'date_of_use', 'amount',)
    search_fields = ('date_of_use',)
    empty_value_display = '-пусто-'
