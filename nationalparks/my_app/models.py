from django.db import models
from django.urls import reverse



DIFFICULTY = (
    ('E', 'Easy'),
    ('M', 'Moderate'),
    ('D', 'Difficult')
)

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


class Trail(models.Model):
    name = models.CharField(max_length=255)
    difficulty = models.CharField(
        max_length=1,
        choices = DIFFICULTY, 
        default = DIFFICULTY[0][0]
        )

    description = models.CharField(max_length=255)

    national_park = models.ForeignKey(NationalPark, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.get_difficulty_display()} on {self.name}"
