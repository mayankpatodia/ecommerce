from django import forms


# Login form
class LoginForm(forms.Form):
    email = forms.CharField(label="email",max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


# Signup form
class SignUpForm(forms.Form):
    fullname = forms.CharField(label="fullname",max_length=100)
    email = forms.CharField(label="email",max_length=100)
    password = forms.CharField(label="password",max_length=100)
    confirm_password = forms.CharField(label="confirm_password", max_length=100)


# Admin Login form
class AdminLoginForm(forms.Form):
    email = forms.CharField(label="email",max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


# Add / Update Product form
class ProductForm(forms.Form):
    name = forms.CharField(label="name",max_length=100)
    image_url = forms.ImageField()
    description = forms.CharField(max_length=250)
    price = forms.DecimalField(max_digits=5,decimal_places=0)


# User Update form
class Ec_UserForm(forms.Form):
    fullname = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)
