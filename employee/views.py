# the landing page for employees

from django.urls import reverse
from django.shortcuts import *
from .models import Employees
from .forms import CreateEmployeeForm
from django.contrib import messages
from django_tables2 import SingleTableView
from .tables import EmployeeTable


class EmployeeLandingView(SingleTableView):
    model = Employees
    table_class = EmployeeTable
    template_name = 'employee/employeeLandingView.html'


def createEmployee(request):

    if request.method == "POST":
        form = CreateEmployeeForm(request.POST)

        if form.is_valid():
            # later implement if the employee already exists then throw error
            form.save()
            messages.success(request, 'Created successfully')

        else:
            return render(request, "employee/createEmployee.html", {
                "form": form
            })

    return render(request, "employee/createEmployee.html", {
        "form": CreateEmployeeForm
    })

# editEmployee instance


def editEmployee(request):
    pass
