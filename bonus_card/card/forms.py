from django import forms

from card.models import Applying


class ApplyingForm(forms.ModelForm):
    class Meta:
        model = Applying
        fields = ('date_of_use', 'amount',)
        labels = {
            'date_of_use': 'Дата использования',
            'amount': 'Сумма',
        }