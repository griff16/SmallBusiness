from django.urls import path
from .views import createEmployee, employeeLandingView


urlpatterns = [
    path('employee/', employeeLandingView, name='employee_landing_view'),
    path('employee/create', createEmployee, name='employee_create'),
]

