from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from datetime import datetime

from .decorators import is_admin
from product.forms import ProductForm, CategoryForm, TagForm
from product.models import Product, Category, Tag
from order.models import Order


def home(request):
    featured_products = Product.objects.featured()
    context = {'products': featured_products}
    return render(request, 'home.html', context)


def about(request):
    context = {}
    return render(request, 'about.html', context)


def contact(request):
    context = {}
    return render(request, 'contact.html', context)


@is_admin
def dashboard(request):
    orders = Order.objects.filter(
        ordered=True, being_delivered=False).order_by('ordered_date')
    month = datetime.now().month
    order_pending = Order.objects.filter(
        ordered=True, being_delivered=False, ordered_date__month=month)
    order_complete = Order.objects.filter(
        ordered=True, being_delivered=True, ordered_date__month=month)
    pending = order_pending.count()
    complete = order_complete.count()
    context = {'orders': orders, 'pending': pending, 'complete': complete}
    return render(request, 'dashboard/dashboard.html', context)


@is_admin
def order_summary(request, ref_id):
    order = get_object_or_404(Order, ref_id=ref_id)
    items = order.orderitem_set.all()
    context = {'order': order, 'items': items}
    return render(request, 'dashboard/order_summary.html', context)


@is_admin
def add_product(request):
    form = ProductForm(data=request.POST or None, files=request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            product = form.save()
            messages.success(
                request, f"{product.title} is added successfully.")
            return redirect(product.get_absolute_url())

    context = {'form': form}
    return render(request, 'dashboard/add_product.html', context)


@is_admin
def all_products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'dashboard/products.html', context)


@is_admin
def category(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        cat = form.save()
        return redirect('category')
    categories = Category.objects.all()
    context = {'categories': categories, 'form': form}

    return render(request, 'dashboard/category.html', context)


@is_admin
def tag(request):
    form = TagForm(request.POST or None)
    if form.is_valid():
        tag = form.save()
        return redirect('tag')
    tags = Tag.objects.all()
    context = {'tags': tags, 'form': form}

    return render(request, 'dashboard/tag.html', context)
