# products/urls.py

from django.conf.urls import url
from products import views
from django.conf import settings
from django.views.static import serve
import django.contrib.auth.views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^login/', views.login),
    url(r'^login/[0-9]+', views.login),
    # url(r'^register_user',views.register_user,name='register_user'),
    url(r'^register', views.register),
    url(r'^products', views.products),
    url(r'^logout', views.logout_user),
    url(r'^product_detail', views.product_details),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),
    ]

