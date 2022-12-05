from django.shortcuts import render
from django.core.paginator import Paginator
from card.models import Applying, Card
from django.shortcuts import get_object_or_404, redirect
from card.forms import ApplyingForm


CARDS_PER_PAGE = 5


def index(request):
    template = 'index.html'
    title = 'Бонусные карты'
    card_list = Card.objects.order_by('-release_date')
    paginator = Paginator(card_list, CARDS_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'title': title,
        'page_obj': page_obj,
    }
    return render(request, template, context)


def card_detail(request, card_id):
    card = get_object_or_404(Card, pk=card_id)
    series = card.series
    number = card.number
    release_date = card.release_date
    end_date = card.end_date
    card_status = card.card_status
    template = 'card_detail.html'
    applyings = card.applying.all()
    form = ApplyingForm()
    context = {
        'card': card,
        'title': f'{series} {number}',
        'series': series,
        'number': number,
        'release_date': release_date,
        'end_date': end_date,
        'card_status': card_status,
        'applyings': applyings,
        'form': form,
    }
    return render(request, template, context)


def add_applying(request, card_id):
    card = get_object_or_404(Card, pk=card_id)
    form = ApplyingForm(request.POST or None)
    if form.is_valid():
        applying = form.save(commit=False)
        applying.card = card
        applying.save()
    return redirect('card:card_detail', card_id=card_id) 
