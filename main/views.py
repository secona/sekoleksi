from django.core import serializers
from django.http import HttpResponse
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

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize('xml', data), content_type='application/xml')

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('xml', data), content_type='application/xml')

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')

