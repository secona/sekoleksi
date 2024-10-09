from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.core import serializers
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
from datetime import datetime
from .forms import ProductForm
from .models import Product

@login_required(login_url='/login')
def show_main(request: HttpRequest):
    return render(request, "main.html", {
        "name": request.user.username,
        "npm": "2306152411",
        "class": "F",
        "last_login": request.COOKIES['last_login'],
    })

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
        else:
            return render(request, 'register.html', { 'form': form })

    form = UserCreationForm()
    return render(request, 'register.html', { 'form': form })

def login_user(request: HttpRequest):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            response = HttpResponseRedirect(reverse('main:show_main'))
            response.set_cookie('last_login', datetime.now().strftime("%c"))
            return response
        else:
            messages.error(request, "Invalid username or password. Please try again.")

    form = AuthenticationForm(request)
    return render(request, 'login.html', { 'form': form })

def logout_user(request: HttpRequest):
    logout(request)
    return redirect('main:login')

@login_required(login_url='/login')
def create_product(request: HttpRequest):
    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form_entry = form.save(commit=False)
            form_entry.user = request.user
            form_entry.save()
            return redirect('main:show_main')

        return redirect('main:show_main')

    form = ProductForm()
    return render(request, 'create_product.html', { 'form': form })

@csrf_exempt
@require_POST
def create_product_ajax(request):
    product_form = ProductForm(
        data={
            "name": strip_tags(request.POST.get('name')),
            "price": strip_tags(request.POST.get('price')),
            "description": strip_tags(request.POST.get('description')),
        },
    )

    if product_form.is_valid():
        product = product_form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponse(b"CREATED", status=201)
    else:
        return HttpResponse(str(product_form.errors.as_json()), status=400)

@login_required(login_url='/login')
def show_product(request: HttpRequest, id):
    product = Product.objects.get(id=id, user_id=request.user.id);
    return render(request, 'view_product.html', { 'product': product })

@login_required(login_url='/login')
def update_product(request: HttpRequest, id):
    obj = get_object_or_404(Product, id=id, user_id=request.user.id)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=obj)

        if form.is_valid():
            form.save()
            return redirect('main:show_main')

        return redirect('main:show_main')

    form = ProductForm(instance=obj)
    return render(request, 'update_product.html', { 'form': form })

@login_required(login_url='/login')
def delete_product(request: HttpRequest, id):
    obj = get_object_or_404(Product, id=id, user_id=request.user.id)

    if request.method == 'POST':
        obj.delete()
        return redirect('main:show_main')

    return render(request, 'delete_product.html', { 'product': obj })

def show_xml(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('xml', data), content_type='application/xml')

def show_xml_by_id(_, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('xml', data), content_type='application/xml')

def show_json(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')

def show_json_by_id(_, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')

