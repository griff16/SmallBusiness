from django.urls import path
from .views import createEmployee, EmployeeLandingView


urlpatterns = [
    path('employee/', EmployeeLandingView.as_view(),
         name='employee_landing_view'),
    path('employee/create', createEmployee, name='employee_create'),
]
