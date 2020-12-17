from django.urls import path
from .views import Store, Product_detail, product_category_detail

urlpatterns = [
    path('', Store.as_view(), name="store"),
    path(
        'category/<slug:slug>/',
        product_category_detail,
        name="category_detail"
    ),
    path('<slug:slug>/', Product_detail.as_view(), name="product_detail"),
]
