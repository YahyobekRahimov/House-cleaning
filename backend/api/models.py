from django.db import models

# Create your models here.
class Endpoint(models.Model):
    country = models.CharField(max_length=10, blank=True, null=True)
    region = models.CharField(max_length=10, blank=True, null=True)
    district = models.CharField(max_length=10, blank=True, null=True)
    village = models.CharField(max_length=10, blank=True, null=True)
    user = models.CharField(max_length=10, blank=True, null=True)
    position = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    location = models.CharField(max_length=10, blank=True, null=True)
    measurment = models.CharField(max_length=10, blank=True, null=True)
    pricing = models.CharField(max_length=10, blank=True, null=True)
    category = models.CharField(max_length=10, blank=True, null=True)
    service = models.CharField(max_length=10, blank=True, null=True)
    order = models.CharField(max_length=10, blank=True, null=True)
    comment = models.CharField(max_length=10, blank=True, null=True)
    visit = models.CharField(max_length=10, blank=True, null=True)
    servicephoto = models.CharField(max_length=10, blank=True, null=True)
    visitphoto = models.CharField(max_length=10, blank=True, null=True)
    video = models.CharField(max_length=10, blank=True, null=True)
    link = models.CharField(max_length=10, blank=True, null=True)
    branchphone = models.CharField(max_length=10, blank=True, null=True)
    branch = models.CharField(max_length=10, blank=True, null=True)
    endpoint = models.CharField(max_length=10, blank=True, null=True)

