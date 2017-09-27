# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Ec_User
from .models import Ec_Admin
from .models import Product
from .forms import *
from django.shortcuts import render


# Create your views here.
# Home page
def home(request):
    user_email = request.session.get('email')
    if not user_email:
        return render(request, 'index.html', {'res': 2})
    user = Ec_User.objects.get(email=user_email)
    return render(request, 'index.html', {'res': 1, 'user': user})


# Login page
def login(request, res=None):
    form = LoginForm()
    d = request.GET.get('res', None)

    # Check user already logged in
    email = request.session.get('email')
    if not email:
        return render(request,'login.html',{'form':form, 'res': d})
    else:
        user = Ec_User.objects.get(email=email)
        Prods = Product.objects.all()
        return redirect('/products/')


# Register page
def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            n = form.cleaned_data['fullname']
            e = form.cleaned_data['email']
            p = form.cleaned_data['password']
            cp = form.cleaned_data['confirm_password']
            # check passwords
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
        # Check user already logged in
        email = request.session.get('email')
        if not email:
            return render(request, 'register.html', {'res': 0})
        else:
            # user = Ec_User.objects.get(email=email)
            # Prods = Product.objects.all()
            return redirect('/products/')


# View Products page
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
            return redirect('/login?res=2')
    else:
        email = request.session.get('email')
        if not email:
            return redirect('/login?res=3')
        else:
            user = Ec_User.objects.get(email=email)
            Prods = Product.objects.all()
            return render(request, 'products.html', {'res': 1, 'user': user, 'Prods': Prods})


# Logout user
def logout_user(request):
    request.session['email'] = None
    return redirect('/login?res=0')


# ----------------------------- ADMIN -----------------------------

# Admin login
def admin_login(request, res=None):
    form = AdminLoginForm()
    return render(request,'admin_login.html',{'form':form})


# Admin home
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


# Admin logout
def admin_logout(request):
    return redirect('/admin_login?res=0')


# Admin view user details
def admin_users(request, res=None):
    Users = Ec_User.objects.all()
    d = request.GET.get('res', None)
    return render(request, 'view_users.html', {'res': d, 'Users': Users})


# Admin view product details
def admin_products(request, res=None):
    Products = Product.objects.all()
    d = request.GET.get('res', None)
    return render(request, 'view_products.html', {'res': d, 'Products': Products})


# Admin add product
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            image_url = form.cleaned_data['image_url']
            product = Product(name=name,description=description, price=price,
                                                                    image_url=image_url)
            product.save()
            return redirect('/admin_products/')
    else:
        form = ProductForm()
        return render(request,'add_product.html',{'form':form})


# Admin delete product
def delete_product(request, pid):
    Product.objects.filter(product_id=pid).delete()
    return redirect('/admin_products/')


# Admin update product
def update_product(request, pid):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            prod = Product.objects.get(product_id=pid)
            prod.name = form.cleaned_data['name']
            prod.description = form.cleaned_data['description']
            prod.price = form.cleaned_data['price']
            prod.image_url = request.FILES['image_url']
            prod.save()
            return redirect('/admin_products?res=2')
        else:
            return redirect('/admin_products?res=1')
    else:
        form = ProductForm()
        prod = Product.objects.get(product_id = pid)
        return render(request,'edit_product.html',{'form':form,'prod': prod})


# Admin delete user
def delete_user(request, uid):
    Ec_User.objects.filter(user_id=uid).delete()
    return redirect('/admin_users/')


# Admin update user data
def update_user(request, uid):
    if request.method == "POST":
        form = Ec_UserForm(request.POST)
        if form.is_valid():
            user = Ec_User.objects.get(user_id=uid)
            user.fullname = form.cleaned_data['fullname']
            user.email = form.cleaned_data['email']
            user.password = form.cleaned_data['password']
            user.save()
            return redirect('/admin_users?res=2')
        else:
            return redirect('/admin_users?res=1')
    else:
        form = Ec_UserForm()
        user = Ec_User.objects.get(user_id = uid)
        return render(request,'edit_user.html',{'form':form,'user': user})

