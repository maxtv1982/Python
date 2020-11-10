from django.db import models


class Table(models.Model):

    name = models.TextField()
    width = models.IntegerField(null=True, default=3)
    number = models.IntegerField()


class File(models.Model):

    name = models.CharField(max_length=30)
    path = models.CharField(max_length=70)

