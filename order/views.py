from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
import json
import string
import random
import datetime
import threading

from account.models import User, Customer, GuestUser
from address.form import ShippingAddressForm, BillingAddressForm, CustomerForm
from address.models import ShippingAddress, BillingAddress, State
from .models import Order, OrderItem
from product.models import Product
from main.utils import cookieCart, cartData, guestUser


class EmailThread(threading.Thread):
    def __init__(self, customer, email_message,  *args, **kwargs):
        self.customer = customer
        self.email_message = email_message
        threading.Thread.__init__(self)

    def run(self):
        self.customer.email_customer(
            self.email_message['subject'],
            self.email_message['message'],
            self.email_message['from_email']
        )


def cart(request):
    return render(request, 'cart.html')


def checkout(request):
    customer_form = CustomerForm()
    form_s = ShippingAddressForm()
    form_b = BillingAddressForm()
    context = {
        'form_s': form_s,
        'form_b': form_b,
        'customer_form': customer_form
    }

    return render(request, 'checkout.html', context)


def update_cart(request):
    if request.method == "POST":
        data = json.loads(request.body)
        productId = data['productid']
        action = data['action']
        customer = request.user.customer
        product = Product.objects.get(id=productId)
        order, created = Order.objects.get_or_create(
            customer=customer, ordered=False)
        orderItem, created = OrderItem.objects.get_or_create(
            order=order, product=product)

        if action == "add":
            orderItem.quantity += 1
        if action == "remove":
            orderItem.quantity -= 1
        orderItem.save()

        if orderItem.quantity <= 0:
            orderItem.delete()

    cData = cartData(request)
    order = cData['order']
    items = cData['items']
    cartItems = cData['cartItems']
    cart_section = render_to_string(
        'components/cart.html', {'order': order, 'items': items, 'cartItems': cartItems})
    cart_icon = render_to_string('components/cart-icon.html', {'order': order})

    return JsonResponse({"message": "Product added", 'cart_icon': cart_icon, "cart_section": cart_section}, safe=False)


def processOrder(request):
    data = json.loads(request.body)
    ref_id = ''.join(random.choices(
        string.ascii_uppercase + string.ascii_lowercase + string.digits, k=20))

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, ordered=False)
    else:
        customer, order = guestUser(request, data)

    total = float(data['form']['total'])

    order.ref_id = ref_id
    order.ordered_date = datetime.datetime.now()

    if total == order.get_cart_total:
        order.ordered = True
        # send email
        # email_message = {
        #     'subject': "Order Successfull placed",
        #     'message': f"Hello {customer.get_full_name}, your order no. {order.id} is placed successfully.",
        #     'from_email': 'djangotest857@gmail.com',
        # }
        # customer.email_customer(
        #     email_message['subject'],
        #     email_message['message'],
        #     email_message['from_email']
        # )

    state_s = State.objects.get(id=int(data['shipping']['state']))
    state_b = State.objects.get(id=int(data['billing']['state']))

    shipping = ShippingAddress.objects.create(
        customer=customer,
        order=order,
        address_s=data['shipping']['address'],
        city_s=data['shipping']['city'],
        state_s=state_s,
        zip_code_s=data['shipping']['zipcode'],
    )

    billing = BillingAddress.objects.create(
        customer=customer,
        order=order,
        address_b=data['billing']['address'],
        city_b=data['billing']['city'],
        state_b=state_b,
        zip_code_b=data['billing']['zipcode'],
    )
    order.shipping_address = shipping
    order.billing_address = billing
    order.save()

    return JsonResponse("PAYMENT COMPLETE", safe=False)
