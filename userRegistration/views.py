from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages


# Create your views here.
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