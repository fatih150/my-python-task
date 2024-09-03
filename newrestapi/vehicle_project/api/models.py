from django.db import models

class Vehicle(models.Model):
    gruppe = models.CharField(max_length=100)
    kurzname = models.CharField(max_length=100)
    langtext = models.TextField()
    info = models.TextField()
    lagerort = models.CharField(max_length=100)
    labelIds = models.TextField(blank=True, null=True)
    rnr = models.CharField(max_length=100, blank=True, null=True)  
    hu = models.CharField(max_length=100, blank=True, null=True)  
