from .models import Currency
from product.models import Category, Product
from order.models import Order, OrderItem
from account.models import *
import json


def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}
    order = {
        'get_cart_total': 0,
        'get_cart_items': 0,
        'shipping': False,
    }
    items = []
    cartItems = order['get_cart_items']
    for i in cart:
        quantity = cart[i]['quantity']
        cartItems += quantity

        product = Product.objects.get(id=i)
        total = product.get_price * quantity

        order['get_cart_total'] += total
        order['get_cart_items'] += quantity

        item = {
            'product': {
                'id': product.id,
                'title': product.title,
                'get_price': product.get_price,
                'imageURL': product.imageURL
            },
            'quantity': quantity,
            'get_total': total
        }

        items.append(item)

    return {'order': order, 'items': items, 'cartItems': cartItems}


def cartData(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, ordered=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']

    return {'cartItems': cartItems, 'order': order, 'items': items}


def guestUser(request, data):
    print('User is not logged in')
    print('COOKIES: ', request.COOKIES)
    first_name = data['form']['first_name']
    last_name = data['form']['last_name']
    email = data['form']['email']
    phone_number = data['form']['phone_number']

    customer, created = Customer.objects.get_or_create(email=email)
    customer.first_name = first_name
    customer.last_name = last_name
    customer.phone_number = phone_number
    customer.save()

    guestu, created = GuestUser.objects.get_or_create(customer=customer)

    order = Order.objects.create(
        customer=customer,
        ordered=False
    )
    cookieData = cookieCart(request)
    items = cookieData['items']

    for item in items:
        product = Product.objects.get(id=item['product']['id'])
        orderItem = OrderItem.objects.create(
            product=product,
            quantity=item['quantity'],
            order=order,
        )

    return customer, order
