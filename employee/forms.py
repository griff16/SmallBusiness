from django.forms import widgets
from employee.models import Employees
from django.db import models
from django.forms import ModelForm
from django.forms.widgets import DateInput


class CreateEmployeeForm(ModelForm):
    class Meta:
        model = Employees
        fields = '__all__'
        labels  = {
            'name' : 'Employee Name',
            'dateOfBirth' : 'Date of Birth',
            'gender' : 'Gender',
            'phone' : 'Phone',
            'address' : 'Address',
            'nationality' : 'Nationality',
        }
        widgets = {
            'dateOfBirth': DateInput(attrs={'type': 'date'})
        }