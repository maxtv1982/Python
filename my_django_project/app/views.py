from django.http import HttpResponse
from django.shortcuts import render, reverse
from django.utils import timezone
from os import listdir
from django.conf import settings
from datetime import datetime

def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir'),
        'контакты': reverse('contact')
    }

    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = f"текущее время {timezone.localtime()}"
    return HttpResponse(f'Текущее время: {current_time}')


def workdir_view(request):
    workdir = listdir('.')
    return HttpResponse(f'содержимое рабочей директории: {workdir}')


def contact_view(request):
    msg = f'Свяжитесь с админом {settings.CONTACT_EMAIL}'
    return HttpResponse('Всем привет! Я Django! ' + msg)


def since_view(request, date):
    dt = datetime.strptime(date, '%Y-%m-%d')
    days = (datetime.now() - dt).days
    return HttpResponse(days)
