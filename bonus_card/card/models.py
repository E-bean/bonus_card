from django.db import models
from django.utils.translation import ugettext_lazy as _


class Appling(models.Model):
    date_of_use = models.DateTimeField(
        auto_now_add=True,
        verbose_name='date of use',
    )
    amount = models.PositiveIntegerField(
        verbose_name='purchase amount',
    )

    def __str__(self):
        return self.date_of_use


class Card(models.Model):
    ACTIVATED = 'activated'
    NOTACTIVATED = 'not activated'
    OVERDUE = 'overdue'
    STATUS_CARD = [
        (ACTIVATED, _('activated')),
        (NOTACTIVATED, _('activated')),
        (OVERDUE, _('overdue'))
    ]
    series = models.PositiveIntegerField(
        verbose_name='series number for card',
    )
    number = models.PositiveIntegerField(
        verbose_name='card number',
    )
    release_date = models.DateTimeField(
        verbose_name='card release date',
        auto_now_add=True,
    )
    end_date = models.DateTimeField(
        verbose_name='end date of card activity',
    )
    appling = models.ForeignKey(
        Appling,
        on_delete=models.CASCADE,
        related_name='cards',
        verbose_name='card usage',
        blank=True,
        null=True,
    )
    card_status = models.CharField(
        max_length=12,
        choices=STATUS_CARD,
        default=NOTACTIVATED,
    )

    def __str__(self):
        return self.number
