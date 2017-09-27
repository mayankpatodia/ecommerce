# products/urls.py

from django.conf.urls import url
from products import views
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    # Home page
    url(r'^$', views.home),

    # Login user
    url(r'^login/', views.login),
    url(r'^login/[0-9]+', views.login),

    # Register and logout user
    url(r'^register', views.register),
    url(r'^logout', views.logout_user),

    # user view products
    url(r'^products', views.products),

    # Admin login and logout
    url(r'^admin_login/', views.admin_login),
    url(r'^admin_home/', views.admin_home),
    url(r'^admin_logout/', views.admin_logout),

    # Admin view users and Products
    url(r'^admin_users/', views.admin_users),
    url(r'^admin_products/', views.admin_products),

    # Add / Delete / Update Product
    url(r'^add_product/', views.add_product),
    url(r'^delete_product/(?P<pid>[0-9]+)/', views.delete_product),
    url(r'^update_product/(?P<pid>[0-9]+)/', views.update_product),

    # Admin Delete / Update Product
    url(r'^delete_user/(?P<uid>[0-9]+)/', views.delete_user),
    url(r'^update_user/(?P<uid>[0-9]+)/', views.update_user),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),
    ]

