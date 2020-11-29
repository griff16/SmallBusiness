from django.urls import path
from .views import listView


urlpatterns = [
    path('employee/', listView, name='list_view'),
]

