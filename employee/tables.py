# employees/tables.py
import django_tables2 as tables
from .models import Employees


class EmployeeTable(tables.Table):
    class Meta:
        model = Employees
        template_name = "django_tables2/bootstrap.html"
        fields = ('id_auto', 'name', 'phone', 'email', 'dateOfBirth')
