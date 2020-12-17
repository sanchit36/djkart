from .models import Currency
from product.models import Category
from order.models import Order

from .utils import cartData


def currency(request):
    return {'curr': Currency.objects.get(id=1)}


def categories(request):
    return {'category_menu': Category.objects.all().exclude(id=1)}


def info(request):
    data = cartData(request)
    order = data['order']
    items = data['items']
    cartItems = data['cartItems']

    return {'order': order, 'items': items, 'cartItems': cartItems}
