# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Ec_User
from .models import Product
from .forms import *
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'index.html', {})


def login(request, res=None):
    form = LoginForm()
    d = request.GET.get('res', None)
    request.session['email'] = None
    return render(request,'login.html',{'form':form, 'res': d})


def register(request):
    request.session['email'] = None
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
    return render(request, 'register.html', {'res': 0})


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
    return redirect('/login?res=0')
