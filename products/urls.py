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

    url(r'^admin_login/', views.admin_login),
    url(r'^admin_home/', views.admin_home),
    url(r'^admin_logout/', views.admin_logout),
    url(r'^admin_users/', views.admin_users),
    url(r'^admin_products/', views.admin_products),
    url(r'^add_product/', views.add_product),
    url(r'^delete_product/', views.delete_product),
    url(r'^update_product/(?P<pid>[0-9]+)/', views.update_product),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),
    ]

