from django.urls import path
from .views import (
    about,
    contact,
    home,
    dashboard,
    order_summary,
    add_product,
    all_products,
    category,
    tag
)

urlpatterns = [
    path('', home, name="home"),
    path('contact/', contact, name="contact"),
    path('about/', about, name="about"),
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/add-product/', add_product, name='add_product'),
    path('dashboard/all-product/', all_products, name='all_product'),
    path('dashboard/category/', category, name='category'),
    path('dashboard/tag/', tag, name='tag'),
    path('dashboard/order-summary/<slug:ref_id>/',
         order_summary, name='order_summary'),
]
