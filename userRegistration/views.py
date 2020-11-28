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

# # Login View
# def login(request):
    
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         user = authenticate(username=form.username, password=form.password)

#         if user is not None:
#             return HttpResponse(form.username)
#         else:
#             return HttpResponse('No user found')
    
#     else:
#         form = LoginForm()
    
#     render(request, "userRegistration/login.html", {"form":form})