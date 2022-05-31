from django import template
from home.models import *
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User

register = template.Library()

@register.simple_tag
def number_of_messages(request):

    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0}
    
    n = OrderItem.objects.count()
    context = {'items':items, 'n':n, 'order':order}
    return render(request, 'cart.html', context)