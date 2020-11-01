from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article, Scopes, Membership


def articles_list(request):
    # тэги - Космос, Наука, Культура, Город, Здоровье, Международные отношения
    template = 'articles/news.html'
    object_list = Article.objects.all()
    scopes = Scopes.objects.all().order_by('scope')

    # for article in object_list:
    #     scope = article.membership_set.all()
    #     scopes.append(scope.order_by('scope'))
    #     # for sc in scope.order_by('scope'):

    # a = Membership.objects.filter(article__title=arty).filter(is_main=True)
    # arty.membership_set.all()
    context = {'object_list': object_list, 'scopes': scopes}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    return render(request, template, context)
