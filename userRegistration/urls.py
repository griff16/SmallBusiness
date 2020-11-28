from django.urls import path
from .views import signUpPage, homeView


urlpatterns = [
    path('', homeView, name='home'),  # temporary homepage
    path('signup/', signUpPage, name='signup'),
]

