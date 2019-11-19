from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Strain_validator(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['strain_name']) < 2:
            errors['strain_name'] = "Name of strain must be at least 2 characters."
        if len(postData['grower']) < 2:
            errors['grower'] = "Grower name must be at least 2 characters."
        if len(postData['dispensary']) < 2:
            errors['dispensary'] = "Dispensary name must be at least 2 characters."
        if len(postData['cannabis']) is None:
            errors['cannabis'] = "Null Cannabis field error."
        if len(postData['medium']) is None:
            errors['medium'] = "Null Medium field error."
        if not postData['price'] or float(postData['price']) <= 0.00:
            errors['price'] = "Price must be listed, and above $0.00"
        if len(postData['amount']) is None:
            errors['amount'] = "Null Amount field error."
        if len(postData['rating']) is None:
            errors['rating'] = "Null Rating field error."
        return errors

class Strain(models.Model):
    strain_name = models.CharField(max_length=255)
    grower = models.CharField(max_length=255)
    dispensary = models.CharField(max_length=255)
    cannabis = models.CharField(max_length=255)
    medium = models.CharField(max_length=255)
    rating = models.IntegerField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    amount = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Strain_validator()