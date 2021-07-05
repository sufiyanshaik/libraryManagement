from django.db import models
from django.urls import reverse
# Create your models here.
class Book(models.Model):
    Name=models.CharField(max_length=60)
    Author=models.CharField(max_length=60)
    Pages=models.IntegerField()
    Cost=models.FloatField()
    def get_absolute_url(self):
        return reverse('home')
