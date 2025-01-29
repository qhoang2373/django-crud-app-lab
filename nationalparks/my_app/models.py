from django.db import models

# Create your models here.
class NationalPark(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255) 
    description = models.TextField()
    established_date = models.DateField() 

    def __str__(self):
        return self.name