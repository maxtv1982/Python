from collections import Counter

from django.shortcuts import render

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
# counter_show = Counter()
# counter_click = Counter()
counter_original = 0
counter_test = 0
counter_all = 0


def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    ind = request.GET.get('from-landing')
    global counter_all
    if ind == 'original':
        global counter_original
        counter_original += 1
        counter_all += 1
        return render(request, 'index.html')
    elif ind == 'test':
        global counter_test
        counter_test += 1
        counter_all += 1
        return render(request, 'index.html')
    else:
        pass


def landing(request):
    ab_test_arg = request.GET.get('ab-test-arg')
    if ab_test_arg == 'original':
        return render(request, 'landing.html')
    elif ab_test_arg == 'test':
        return render(request, 'landing_alternate.html')
    else:
        return render(request, 'index.html')


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Для вывода результат передайте в следующем формате:
    return render(request, 'stats.html', context={
        'test_conversion': f"{counter_test} / {counter_all}",
        'original_conversion': f"{counter_original} / {counter_all}",
    })
