from django.shortcuts import render, redirect
from .forms import RegisterForm


# Create your views here.
def signUpPage(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("www.google.com")

    else:
	    form = RegisterForm()

    return render(response, "userRegistration/signup.html", {"form":form})