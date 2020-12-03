from django.urls import reverse
from django.shortcuts import *
from .models import Employees
from .forms import CreateEmployeeForm
from django.contrib import messages

# the landing page for employee
def employeeLandingView(request):  
    return render(request, 'employee/employeeLandingView.html')

# create employee instance
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

