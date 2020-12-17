from django.urls import path
from .views import cart, checkout, update_cart, processOrder

urlpatterns = [
    path('cart/', cart, name="cart"),
    path('checkout/', checkout, name="checkout"),
    path('update_cart/', update_cart, name="update_cart"),
    path('process_order/', processOrder, name="process_order"),
]
