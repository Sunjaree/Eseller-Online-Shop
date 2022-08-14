from django.shortcuts import render,HttpResponse,redirect
import datetime

from home.models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 
import os
from django.core.mail import send_mail

from django.db import models
from django.http import JsonResponse
import json




def index(request):

    params = {}
    if request.user.is_authenticated:
        customer = request.user

        if Order.objects.filter(customer=customer,complete=False).count():
            order = Order.objects.get(customer=customer,complete=False)
            number_of_product_in_cart = order.get_cart_items
        else:
            number_of_product_in_cart = 0

        params = {'number_of_product_in_cart': number_of_product_in_cart}
    


    return render(request,'index.html',params)
    #return HttpResponse("Hi, How u doin?")


def about(request):

    customer = request.user
    if request.user.is_authenticated and Order.objects.filter(customer=customer,complete=False).count():
        order = Order.objects.get(customer=customer,complete=False)
        number_of_product_in_cart = order.get_cart_items
    else:
        number_of_product_in_cart = 0
            
    params = {'number_of_product_in_cart': number_of_product_in_cart}

    return render(request,'about.html',params)


# Client Contact
def contact(request):
    
    params = {}
    if request.user.is_authenticated:
        customer = request.user

        if Order.objects.filter(customer=customer,complete=False).count():
            order = Order.objects.get(customer=customer,complete=False)
            number_of_product_in_cart = order.get_cart_items
        else:
            number_of_product_in_cart = 0

        params = {'number_of_product_in_cart': number_of_product_in_cart}

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        comment = request.POST.get("comment")

        if name!="":
            contact = Contact(name=name,email=email,phone=phone,comment=comment,date=datetime.today())
            contact.save()
            messages.success(request, 'Your response has been submitted successfully!!!')
    return render(request,'contact.html', params)


# Admin Contact view
@login_required(login_url='/login')
def contact_admin(request):
    if request.user.is_superuser :
      contact = Contact.objects.all().filter(is_replied=False).order_by('-date')
      n = Contact.objects.count()
      params = {'contact': contact, 'n':1}
      return render(request,'contact_admin.html',params)

    else:
        return render(request,'html_view_with_error',{"error" : "PERMISSION DENIED"})


# Admin Send Email Through Contact
def sendEmails_contact_admin(request,message_id):
    if request.method=='POST':
        recipient = request.POST.get('recipient_name')
        subject = request.POST.get('email_subject')
        message = request.POST.get('message_text')

        send_mail(
            subject,
            message,
            'eseller.sunjare@gmail.com',
            [recipient],
            fail_silently=False
        )

        contact = Contact.objects.get(pk=message_id)
        contact.is_replied = True
        contact.save()

        Sent_replies.objects.create(message_sender=contact)
        Sent_replies_message_id = Sent_replies.objects.get(message_sender__message_id=message_id)
        Sent_replies_message_id.reply = message
        Sent_replies_message_id.subject = subject
        Sent_replies_message_id.save()

        messages.success(request, 'Message has been sent successfully!!!')
        return redirect("contact_admin")


# Admin Delete Email Through Contact
def deleteEmails_contact_admin(request,message_id):
        message = Contact.objects.get(pk=message_id)
        message.delete()
        return redirect("contact_admin")


# View Sent Replies
@login_required(login_url='/login')
def replies_contact_admin(request):
    if request.user.is_superuser :
        sent_replies = Sent_replies.objects.all()
        params = {'sent_replies': sent_replies}
        return render(request,'replies_contact_admin.html',params)


# Admin Delete Email Through Sent Replies
def deleteEmails_Sent_replies_admin(request,message_id):
        message = Sent_replies.objects.get(message_sender__message_id=message_id)
        message.delete()
        return redirect("replies_contact_admin")


def search(request):
    return HttpResponse("sfsbs")


#For Poducts

def fruit(request):
    product = Product.objects.filter(category="Fruit")
    n = Product.objects.filter(category="Fruit").count()

    
    if request.user.is_authenticated:
        customer = request.user

        if Order.objects.filter(customer=customer,complete=False).count():
            order = Order.objects.get(customer=customer,complete=False)
            number_of_product_in_cart = order.get_cart_items
        else:
            number_of_product_in_cart = 0

        params = {'product': product, 'range':range(1,n), 'n':n, 'number_of_product_in_cart': number_of_product_in_cart}

    else:
        params = {'product': product, 'range':range(1,n), 'n':n}

    return render(request,'fruit.html',params)


def vegetable(request):
    product = Product.objects.filter(category="Vegetable")
    n = Product.objects.filter(category="Vegetable").count()

    
    if request.user.is_authenticated:
        customer = request.user

        if Order.objects.filter(customer=customer,complete=False).count():
            order = Order.objects.get(customer=customer,complete=False)
            number_of_product_in_cart = order.get_cart_items
        else:
            number_of_product_in_cart = 0

        params = {'product': product, 'range':range(1,n), 'n':n, 'number_of_product_in_cart': number_of_product_in_cart}

    else:
        params = {'product': product, 'range':range(1,n), 'n':n}

    return render(request,'vegetable.html',params)



def toy(request):
    product = Product.objects.filter(category="Toy")
    n = Product.objects.filter(category="Toy").count()

    
    if request.user.is_authenticated:
        customer = request.user

        if Order.objects.filter(customer=customer,complete=False).count():
            order = Order.objects.get(customer=customer,complete=False)
            number_of_product_in_cart = order.get_cart_items
        else:
            number_of_product_in_cart = 0

        params = {'product': product, 'range':range(1,n), 'n':n, 'number_of_product_in_cart': number_of_product_in_cart}

    else:
        params = {'product': product, 'range':range(1,n), 'n':n}

    return render(request,'toy.html',params)



def medicine(request):
    product = Product.objects.filter(category="Medicine")
    n = Product.objects.filter(category="Medicine").count()

    
    if request.user.is_authenticated:
        customer = request.user

        if Order.objects.filter(customer=customer,complete=False).count():
            order = Order.objects.get(customer=customer,complete=False)
            number_of_product_in_cart = order.get_cart_items
        else:
            number_of_product_in_cart = 0

        params = {'product': product, 'range':range(1,n), 'n':n, 'number_of_product_in_cart': number_of_product_in_cart}

    else:
        params = {'product': product, 'range':range(1,n), 'n':n}

    return render(request,'medicine.html',params)


def stationery(request):
    product = Product.objects.filter(category="Stationery")
    n = Product.objects.filter(category="Stationery").count()

    
    if request.user.is_authenticated:
        customer = request.user

        if Order.objects.filter(customer=customer,complete=False).count():
            order = Order.objects.get(customer=customer,complete=False)
            number_of_product_in_cart = order.get_cart_items
        else:
            number_of_product_in_cart = 0

        params = {'product': product, 'range':range(1,n), 'n':n, 'number_of_product_in_cart': number_of_product_in_cart}

    else:
        params = {'product': product, 'range':range(1,n), 'n':n}

    return render(request,'stationery.html',params)


def pet(request):
    product = Product.objects.filter(category="Pet")
    n = Product.objects.filter(category="Pet").count()

    
    if request.user.is_authenticated:
        customer = request.user

        if Order.objects.filter(customer=customer,complete=False).count():
            order = Order.objects.get(customer=customer,complete=False)
            number_of_product_in_cart = order.get_cart_items
        else:
            number_of_product_in_cart = 0

        params = {'product': product, 'range':range(1,n), 'n':n, 'number_of_product_in_cart': number_of_product_in_cart}

    else:
        params = {'product': product, 'range':range(1,n), 'n':n}

    return render(request,'pet.html',params)


def electric(request):
    product = Product.objects.filter(category="Electric")
    n = Product.objects.filter(category="Electric").count()

    
    if request.user.is_authenticated:
        customer = request.user

        if Order.objects.filter(customer=customer,complete=False).count():
            order = Order.objects.get(customer=customer,complete=False)
            number_of_product_in_cart = order.get_cart_items
        else:
            number_of_product_in_cart = 0

        params = {'product': product, 'range':range(1,n), 'n':n, 'number_of_product_in_cart': number_of_product_in_cart}

    else:
        params = {'product': product, 'range':range(1,n), 'n':n}

    return render(request,'electric.html',params)


def meat(request):
    product = Product.objects.filter(category="Meat")
    n = Product.objects.filter(category="Meat").count()

    
    if request.user.is_authenticated:
        customer = request.user

        if Order.objects.filter(customer=customer,complete=False).count():
            order = Order.objects.get(customer=customer,complete=False)
            number_of_product_in_cart = order.get_cart_items
        else:
            number_of_product_in_cart = 0

        params = {'product': product, 'range':range(1,n), 'n':n, 'number_of_product_in_cart': number_of_product_in_cart}

    else:
        params = {'product': product, 'range':range(1,n), 'n':n}

    return render(request,'meat.html',params)


def fish(request):
    product = Product.objects.filter(category="Fish")
    n = Product.objects.filter(category="Fish").count()

    
    if request.user.is_authenticated:
        customer = request.user
        if Order.objects.filter(customer=customer,complete=False).count():
            order = Order.objects.get(customer=customer,complete=False)
            number_of_product_in_cart = order.get_cart_items
        else:
            number_of_product_in_cart = 0

        params = {'product': product, 'range':range(1,n), 'n':n, 'number_of_product_in_cart': number_of_product_in_cart}

    else:
        params = {'product': product, 'range':range(1,n), 'n':n}

    return render(request,'fish.html',params)




#Add Product
def add_product(request):
    if request.method=='POST':
        product_name = request.POST['product_name']
        product_category = request.POST['product_category']
        product_price = request.POST['product_price']
        product_photo = request.FILES['product_photo']
        product_description = request.POST['product_description']
    
        add_product = Product(product_name=product_name,category=product_category,price=product_price,description=product_description, pub_date=datetime.today(),image=product_photo)
        add_product.save()

        messages.success(request, 'Product has been added successfully!!!')
        return render(request,'index.html')    

    else:
        return HttpResponse("404-Not Found") 


# For Deleting Product
def delete_product(request,product_id):
    product = Product.objects.get(pk=product_id)
    os.remove(product.image.path)
    product.delete()
    messages.success(request, 'Product has been deleted successfully!!!')
    return redirect("/")


# For Updating Product
def update_product(request,product_id):
    if request.method=='POST':
            product = Product.objects.get(pk=product_id)
            
            product.product_name = request.POST['product_name']
            product.category = request.POST['product_category']
            product.price = request.POST['product_price']

            if 'product_photo' in request.FILES:
                os.remove(product.image.path)
                product.image = request.FILES['product_photo']

            product.description = request.POST['product_description']
            product.pub_date = datetime.today()
            product.save()

            messages.success(request, 'Product has been updated successfully!!!')
            return redirect("/") 
    else:
        return HttpResponse("404-Not Found") 

    
#Handeling Signup + Login + Logout
def handleSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']


        if User.objects.filter(username=username).count()==1:
            messages.warning(request, "This username already exists, Please Choose another!!!")
            return redirect('home')


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


def cart(request):

    customer = request.user
    if request.user.is_authenticated and Order.objects.filter(customer=customer,complete=False).count():
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()

        number_of_product_in_cart = order.get_cart_items
        context = {'items':items, 'number_of_product_in_cart':number_of_product_in_cart, 'order':order}

    else:
        number_of_product_in_cart = 0
        context = {'number_of_product_in_cart':number_of_product_in_cart}

    return render(request, 'cart.html', context)


def checkout(request):

    customer = request.user
    if request.user.is_authenticated and Order.objects.filter(customer=customer,complete=False).count():

        order,created = Order.objects.get_or_create(customer=customer, complete=False)
        # order = Order.objects.get(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        number_of_product_in_cart = order.get_cart_items
        context = {'items': items, 'order': order, 'cartItems': cartItems, 'number_of_product_in_cart': number_of_product_in_cart}
    
    else:
        number_of_product_in_cart = 0
        context = {'number_of_product_in_cart':number_of_product_in_cart}

    return render(request, 'checkout.html', context)


def UpdateItem(request):
    data = json.loads(request.body)
    product_id = data['product_id']
    action = data['action']
    print("Action: ",action)
    print("Product Id: ", product_id)

    customer = request.user
    product = Product.objects.get(product_id=product_id)

    order,created = Order.objects.get_or_create(customer=customer, complete=False)
    # order = Order.objects.get(customer=customer, complete=False)
    orderItem,created = OrderItem.objects.get_or_create(order=order, product=product)

    if action=='add' and orderItem.quantity<5:
        orderItem.quantity = (orderItem.quantity + 1)
    elif action=='remove':
        orderItem.quantity = (orderItem.quantity - 1)
    elif action == 'cancel':
        orderItem.quantity = 0
    else:
        messages.warning(request,"Sorry, You can not add more than 5 same type of item")
    
    orderItem.save()

    if orderItem.quantity<=0:
        orderItem.delete()

    return JsonResponse('Item added', safe=False)


def processOrder(request):
    
    transaction_id = datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user
        order,created = Order.objects.get_or_create(customer=customer, complete=False)
        # order = Order.objects.get(customer=customer, complete=False)
        total = data['shipping']['total']
        order.transaction_id = transaction_id

        if float(total) == order.get_cart_total:
            order.complete = True

        order.save()

        # Order.objects.filter(customer=customer).filter(complete=False).delete()

        ShippingAddress.objects.create(

            customer= request.user,
            order=order,
            first_name = data['shipping']['first_name'],
            last_name = data['shipping']['last_name'],
            username = data['shipping']['username'],
            phone_number = data['shipping']['phone'],
            email = data['shipping']['email'],
            address=data['shipping']['address'],
            
        )

        return JsonResponse('Payment Complete', safe=False)

    else:
        print("not logged in")
        return JsonResponse('item added', safe=False)


def view_order_admin(request):
    customer_order = Order.objects.filter(delivered=False)
    customer_order_items = OrderItem.objects.all()
    n = Product.objects.all()
    params = {'customer_order': customer_order, 'customer_order_items':customer_order_items,'n':n}
    return render(request, 'view_order_admin.html', params)

    