from django.shortcuts import render, redirect
from .forms import RegisterForm


# Create your views here.
def signUpPage(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        
        if form.is_valid():  # if it's valid
            form.save()
            return redirect("/admin")
        
        print(form.errors)
        return redirect("/signup")  # if it's not valid

    else:
	    form = RegisterForm()

    return render(response, "userRegistration/signup.html", {"form":form})