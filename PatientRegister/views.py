from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def insertform(request):
    return render(request,"Register.html")

def userregister(request):
    first_name=request.GET["First_Name"]
    last_name=request.GET["Last_Name"]
    username=request.GET["username"]
    email=request.GET["email"]
    password=request.GET["password"]   
    user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
    user.save()
    messages.info(request,'successfully saved')
    return render(request,"register.html") 


def form(request):
    return render(request,"Searchpatient.html")

def search(request):
    id=request.GET["id"]
    user=User.objects.get(username=id)
    return render(request,"Searchpatient.html",{'user':user})