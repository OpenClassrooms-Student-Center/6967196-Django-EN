from django.db import models


class Band(models.Model):
    name = models.fields.CharField(max_length=100)


class Listing(models.Model):
    title = models.fields.CharField(max_length=100)
