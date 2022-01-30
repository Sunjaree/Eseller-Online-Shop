from unicodedata import category
import django
from django.shortcuts import render,HttpResponse,redirect
from markupsafe import re
from datetime import datetime
from home.models import Contact, Product
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.



def index(request):

    context = {
        "var" : "45265"
    }

    return render(request,'index.html',context)
    #return HttpResponse("Hi, How u doin?")

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'service.html')





def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        comment = request.POST.get("comment")
        if name!="":
            contact = Contact(name=name,email=email,phone=phone,comment=comment,date=datetime.today())
            contact.save()
            messages.success(request, 'Your response has been submitted successfully!!!')
    return render(request,'contact.html')








#For Poducts
def fruit(request):

    product = Product.objects.all()
    n = Product.objects.filter(category="Fruit").count()
    params = {'product': product, 'range':range(1,n), 'n':n}
    return render(request,'fruit.html',params)


def vegetable(request):

    product = Product.objects.all()
    n = Product.objects.filter(category="Vegetable").count()
    params = {'product': product, 'range':range(1,n),'n':n}
    return render(request,'vegetable.html',params)


def toy(request):

    product = Product.objects.all()
    n = Product.objects.filter(category="Toy").count()
    params = {'product': product, 'range':range(1,n),'n':n}
    return render(request,'toy.html',params)


def medicine(request):

    product = Product.objects.all()
    n = Product.objects.filter(category="Medicine").count()
    params = {'product': product, 'range':range(1,n),'n':n}
    return render(request,'medicine.html',params)


def stationery(request):

    product = Product.objects.all()
    n = Product.objects.filter(category="Stationery").count()
    params = {'product': product, 'range':range(1,n),'n':n}
    return render(request,'stationery.html',params)


def pet(request):

    product = Product.objects.all()
    n = Product.objects.filter(category="Pet").count()
    params = {'product': product, 'range':range(1,n),'n':n}
    return render(request,'pet.html',params)


def electric(request):

    product = Product.objects.all()
    n = Product.objects.filter(category="Electric").count()
    params = {'product': product, 'range':range(1,n),'n':n}
    return render(request,'electric.html',params)


def meat(request):

    product = Product.objects.all()
    n = Product.objects.filter(category="Meat").count()
    params = {'product': product, 'range':range(1,n),'n':n}
    return render(request,'meat.html',params)


def fish(request):

    product = Product.objects.all()
    n = Product.objects.filter(category="Fish").count()
    params = {'product': product, 'range':range(1,n),'n':n}
    return render(request,'fish.html',params)







def search(request):
    return HttpResponse("sfsbs")


def checkout(request):
    return HttpResponse("sdvsdvs")



def handleSignup(request):

    if request.method == 'POST':

        #Get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if len(username)>10:
            messages.warning(request, " Your username must be under 10 characters")
            return redirect('home')

        if not username.isalnum():
            messages.warning(request, " User name should only contain letters and numbers")
            return redirect('home')

        if (pass1!= pass2):
             messages.warning(request, " Passwords do not match")
             return redirect('home')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"Your account has been created successfully!!!")
        return redirect('home')

    else:
        return HttpResponse("404-Not Found")   







def handleLogin(request):

    if request.method=='POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername,password=loginpassword)

        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Logged In!!!")
            return redirect('home')
        else:
            messages.warning(request,"Invalid credentials, Please try again :(")
            return redirect('home')

    else:
        return HttpResponse("404-Not Found") 






def handleLogout(request):
    logout(request)
    messages.success(request,"Successfully Loggged Out")
    return redirect('home')
