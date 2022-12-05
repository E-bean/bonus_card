from django.urls import path
from card.views import card_detail, index, add_applying


app_name = 'card'

urlpatterns = [
    path('', index),
    path('cards/<int:card_id>/', card_detail, name='card_detail'),
    path('cards/<int:card_id>/comment/', add_applying, name='add_applying'),
] 