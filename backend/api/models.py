from django.db import models

# Create your models here.
class Endpoint(models.Model):
    endpoints = (
        ('contact', 'contact'),

    )
    name = models.CharField(max_length=128, blank=False, null=True, choices=endpoints)
    key = models.CharField(max_length=10, blank=False, null=True)