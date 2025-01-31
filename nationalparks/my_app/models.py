from django.db import models
from django.urls import reverse


# Create your models here.
class NationalPark(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255) 
    description = models.TextField()
    established_date = models.DateField() 

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('park-detail', kwargs={'park_id': self.id})