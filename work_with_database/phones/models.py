from django.db import models


class Phone(models.Model):
    name = models.TextField()
    price = models.FloatField(null=True)
    image = models.TextField()
    release_date = models.DateField(null=True)
    lte_exists = models.BooleanField(null=True)
    slug = models.SlugField()

