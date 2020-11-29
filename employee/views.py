from django import forms
from django.urls import reverse
from django.shortcuts import render, redirect

# Create your views here.
def listView(request):
    return render(request, 'employee/listView.html')

