from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from django.core.paginator import Paginator

information = []
with open('data-398-2018-08-30.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        information.append({'Name': row['Name'], 'Street': row['Street'], 'District': row['District']})


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    current_page = int(request.GET.get('page', 1))
    paginator = Paginator(information, 15)
    page_obj = paginator.get_page(current_page)
    prev_page, next_page = None, None  # по умолчанию говорим что других страниц нет
    if page_obj.has_previous():  # спрашиваем есть ли предыдущая страница
        prev_page = page_obj.previous_page_number  # получаем её номер
        print(prev_page)
    if page_obj.has_next():  # спрашиваем есть ли следующая страница
        next_page = page_obj.next_page_number  # получаем её номер
        print(next_page)
    return render(request, 'index.html', context={
        'bus_stations': page_obj.object_list,
        'current_page': page_obj.number,
        'prev_page_url': prev_page,
        'next_page_url': next_page,
         })

