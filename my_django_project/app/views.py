from django.http import HttpResponse
from django.shortcuts import render, reverse
from django.utils import timezone
from os import listdir


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
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

