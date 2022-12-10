import random
from datetime import datetime

from dateutil.relativedelta import relativedelta
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from card.forms import ApplyingForm, CardForm
from card.models import Card

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


def card_edit(request, card_id):
    card = get_object_or_404(Card, pk=card_id)
    form = CardForm(
        request.POST or None,
        instance=card
    )
    context = {
        'form': form,
        'card': card}
    if form.is_valid():
        form.save()
        return redirect('card:card_detail', card_id=card_id)
    return render(request, 'card_edit.html', context)


def card_delete(request, card_id):
    Card.objects.filter(id=card_id).delete()
    return redirect('card:index')


def generator(request):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        series = int(request.POST.get('series'))
        period = int(request.POST.get('period'))
        end_date = datetime.now() + relativedelta(months=+period)
        for i in range(quantity):
            number = random.randint(1, 100000)
            while Card.objects.filter(number=number).exists():
                number = random.randint(1, 100000)
            Card.objects.create(
                series=series,
                end_date=end_date,
                number=number
            )
        return redirect('card:index')
    return render(request, 'generator.html')


def search(request):
    if request.method == 'POST':
        series = request.POST.get('series')
        number = request.POST.get('number')
        release_date = request.POST.get('release_date')
        end_date = request.POST.get('end_date')
        card_status = request.POST.get('card_status')
        queryset = Card.objects.all().order_by('id')
        print(card_status == 'all')
        if series != '':
            series = int(series)
            queryset = queryset.filter(series=series).order_by('id')
        if number != '':
            number = int(number)
            queryset = queryset.filter(number=number).order_by('id')
        if release_date != '':
            datetime_obj = datetime.strptime(release_date, '%d %m %Y')
            queryset = queryset.filter(
                release_date__contains=datetime.date(datetime_obj),
                ).order_by('id')
        if end_date != '':
            datetime_obj = datetime.strptime(end_date, '%d %m %Y')
            queryset = queryset.filter(
                end_date__contains=datetime.date(datetime_obj),
                ).order_by('id')
        if card_status != '':
            if card_status != 'all':
                queryset = queryset.filter(
                    card_status=card_status
                ).order_by('id')
        paginator = Paginator(queryset, CARDS_PER_PAGE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'page_obj': page_obj,
        }
        return render(request, 'index.html', context)
    return render(request, 'search.html')
