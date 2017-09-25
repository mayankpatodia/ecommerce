# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Ec_User
from .models import Ec_Admin
from .models import Product
from .forms import *
from django.shortcuts import render


# Create your views here.
def home(request):
    user_email = request.session.get('email')
    if not user_email:
        return render(request, 'index.html', {'res': 2})
    user = Ec_User.objects.get(email=user_email)
    return render(request, 'index.html', {'res': 1, 'user': user})


def login(request, res=None):
    form = LoginForm()
    d = request.GET.get('res', None)
    email = request.session.get('email')
    if not email:
        return render(request,'login.html',{'form':form, 'res': d})
    else:
        user = Ec_User.objects.get(email=email)
        Prods = Product.objects.all()
        return redirect('/products/')



def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            n = form.cleaned_data['fullname']
            e = form.cleaned_data['email']
            p = form.cleaned_data['password']
            cp = form.cleaned_data['confirm_password']
            if p == cp:
                user = Ec_User(fullname = n,
                                  email = e,
                                  password = p)
                user.save()
                return render(request, 'register.html', {'form': form, 'res': 3})
            else:
                return render(request, 'register.html', {'form': form, 'res': 1})
        else:
            return render(request, 'register.html', {'form': form, 'res': 2})
    else:
        email = request.session.get('email')
        if not email:
            return render(request, 'register.html', {'res': 0})
        else:
            user = Ec_User.objects.get(email=email)
            Prods = Product.objects.all()
            return redirect('/products/')




def products(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            e = form.cleaned_data['email']
            p = form.cleaned_data['password']
            try:
                user = Ec_User.objects.get(email = e,
                              password = p)
                request.session['email'] = user.email
                Prods = Product.objects.all()
                return render(request, 'products.html', {'form': form, 'res': 1, 'user': user, 'Prods': Prods})
            except:
                return redirect('/login?res=1')
        else:
            return redirect('/  login?res=2')
    else:
        email = request.session.get('email')
        if not email:
            return redirect('/login?res=3')
        else:
            user = Ec_User.objects.get(email=email)
            Prods = Product.objects.all()
            return render(request, 'products.html', {'res': 1, 'user': user, 'Prods': Prods})



def product_details(request):
    return render(request, 'product_details.html', {})

def logout_user(request):
    request.session['email'] = None
    return redirect('/login?res=0')


def admin_login(request, res=None):
    form = AdminLoginForm()
    return render(request,'admin_login.html',{'form':form})

def admin_home(request, res=None):
    if request.method == "POST":
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            e = form.cleaned_data['email']
            p = form.cleaned_data['password']
            try:
                user = Ec_Admin.objects.get(email = e,
                              password = p)
                return render(request, 'admin_home.html', {'form': form, 'res': 1, 'user': user})
            except:
                return redirect('/admin_login/res=1')
        else:
            return redirect('/admin_login/res=2')
    else:
        return redirect('/admin_login/')


def admin_logout(request):
    return redirect('/admin_login?res=0')


def admin_users(request):
    Users = Ec_User.objects.all()
    return render(request, 'view_users.html', {'res': 1, 'Users': Users})


def admin_products(request):
    Products = Product.objects.all()
    return render(request, 'view_products.html', {'res': 1, 'Products': Products})


def add_product(request):
    request.session['email'] = None
    return redirect('/login?res=0')


def delete_product(request):
    request.session['email'] = None
    return redirect('/login?res=0')


def update_product(request, pid):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            image_url = form.cleaned_data['image_url']
            Product.objects.filter(product_id=pid).update(name=name,description=description, price=price,
                                                                    image_url=image_url)
            return redirect('/admin_products/')
    else:
        form = ProductForm()
        prod = Product.objects.get(product_id = pid)
        return render(request,'edit_product.html',{'form':form,'prod': prod})

