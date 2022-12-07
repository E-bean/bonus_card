from django.urls import path
from card.views import card_detail, index, add_applying, card_edit, card_delete


app_name = 'card'

urlpatterns = [
    path('', index, name='index'),
    path('cards/<int:card_id>/', card_detail, name='card_detail'),
    path('cards/<int:card_id>/comment/', add_applying, name='add_applying'),
    path('cards/<int:card_id>/edit/', card_edit, name='card_edit'),
    path('cards/<int:card_id>/delete/', card_delete, name='card_delete'),
] 