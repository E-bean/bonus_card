from django.db import models
from django.utils.translation import ugettext_lazy as _


class Card(models.Model):
    ACTIVATED = 'activated'
    NOTACTIVATED = 'not activated'
    OVERDUE = 'overdue'
    STATUS_CARD = [
        (ACTIVATED, _('activated')),
        (NOTACTIVATED, _('not activated')),
        (OVERDUE, _('overdue'))
    ]
    series = models.PositiveIntegerField(
        verbose_name='series number for card',
    )
    number = models.PositiveIntegerField(
        verbose_name='card number',
        unique=True,
    )
    release_date = models.DateTimeField(
        verbose_name='card release date',
        auto_now_add=True,
    )
    end_date = models.DateTimeField(
        verbose_name='end date of card activity',
    )
    card_status = models.CharField(
        max_length=13,
        choices=STATUS_CARD,
        default=NOTACTIVATED,
    )

    def __str__(self):
        return str(self.number)


class Applying(models.Model):
    card = models.ForeignKey(
        Card,
        on_delete=models.CASCADE,
        related_name='applying',
        verbose_name='card usage',
    )
    date_of_use = models.DateTimeField(
        verbose_name='date of use',
    )
    amount = models.PositiveIntegerField(
        verbose_name='purchase amount',
    )

    def __str__(self):
        return f'{self.date_of_use} {self.amount}'
