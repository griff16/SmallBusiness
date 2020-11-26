from django.urls import path
from .views import signUpPage


urlpatterns = [
    path('signup/', signUpPage, name='signup'),
]

