from django.urls import path
from .views import loginPage


urlpatterns = [
    path('login/', loginPage, name='signup'),
]

