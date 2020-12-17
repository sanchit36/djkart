from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from product.models import Product, Category


class Store(ListView):
    model = Product
    template_name = 'store.html'
    context_object_name = "products"
    paginate_by = 20


class Product_detail(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'


def product_category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.category(category.slug)
    context = {'category': category, 'products': products}
    return render(request, 'store.html', context)
