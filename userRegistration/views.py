from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate


# SignUp View
def signUpPage(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        
        if form.is_valid():  # if it's valid
            form.save()
            return redirect("/admin")
        
        print(form.errors)

    else:
	    form = RegisterForm()

    return render(response, "userRegistration/signup.html", {"form":form})

# Temp Home View
def homeView(request):
    return render(request, 'userRegistration/tempHome.html')
