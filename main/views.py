from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.core import serializers
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from datetime import datetime
from .forms import ProductForm
from .models import Product

@login_required(login_url='/login')
def show_main(request: HttpRequest):
    products = Product.objects.filter(user=request.user)

    return render(request, "main.html", {
        "name": request.user.username,
        "npm": "2306152411",
        "class": "F",
        "products": products,
        "last_login": request.COOKIES['last_login'],
    })

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')

    form = UserCreationForm()
    return render(request, 'register.html', { 'form': form })

def login_user(request: HttpRequest):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            response = HttpResponseRedirect(reverse('main:show_main'))
            response.set_cookie('last_login', str(datetime.now()))
            return response

    form = AuthenticationForm(request)
    return render(request, 'login.html', { 'form': form })

def logout_user(request: HttpRequest):
    logout(request)
    return redirect('main:login')

def create_product(request: HttpRequest):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        form_entry = form.save(commit=False)
        form_entry.user = request.user
        form_entry.save()
        return redirect('main:show_main')

    return render(request, 'create_product.html', { 'form': form })

def show_xml(_):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize('xml', data), content_type='application/xml')

def show_xml_by_id(_, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('xml', data), content_type='application/xml')

def show_json(_):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')

def show_json_by_id(_, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')

