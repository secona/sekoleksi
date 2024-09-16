from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

def show_main(request):
    products = Product.objects.all()

    return render(request, "main.html", {
        "name": "Muhammad Vito Secona",
        "npm": "2306152411",
        "class": "F",
        "products": products,
    })

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    return render(request, 'create_product.html', { 'form': form })
