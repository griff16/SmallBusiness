from django.shortcuts import HttpResponse

# Create your views here.
def loginPage(reqeust):
    return HttpResponse('this is login page')