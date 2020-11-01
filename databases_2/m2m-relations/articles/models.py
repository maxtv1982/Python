from django.db import models


class ScopesTitle(models.TextChoices):
    CITY = 'Город'
    HEALTH = 'Здоровье'
    CULTURE = 'Культура'
    SPACE = 'Космос'
    SCIENCE = 'Наука'
    RELATIONS = 'Международные отношения'


class Scopes(models.Model):
    scope = models.TextField(choices=ScopesTitle.choices, verbose_name='Раздел')
    # members = models.ManyToManyField(Article, through='Membership')

    def __str__(self):
        return self.scope


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение', )
    scope = models.ManyToManyField(Scopes, through='Membership')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Membership(models.Model):
    article = models.ForeignKey(Article, null=True, on_delete=models.CASCADE)
    scope = models.ForeignKey(Scopes, on_delete=models.CASCADE)
    is_main = models.BooleanField(null=True)
