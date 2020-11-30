from django.db import models
from django_countries.fields import CountryField

# Create your models here.
from django.db import models

class Employees(models.Model):
    name = models.TextField()
    date_of_birth = models.DateField()
    gender = models.NullBooleanField()  # true->female, false->male, null->not specified
    phone =  models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    nationality = CountryField()

    def __str__(self):
        return self.name