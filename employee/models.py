from django.db import models
from django_countries.fields import CountryField

# Create your models here.
from django.db import models


class Employees(models.Model):
    id_auto = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    dateOfBirth = models.DateField()
    gender = models.NullBooleanField(
        choices=[
            (True, 'female'),
            (False, 'male'),
            (None, 'null')
        ]
    )
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=400)
    nationality = CountryField()

    def __str__(self):
        return self.name
