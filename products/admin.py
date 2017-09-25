# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Ec_User
from .models import Product
from .models import Ec_Admin

# Register your models here.
admin.site.register(Ec_User)
admin.site.register(Product)
admin.site.register(Ec_Admin)
