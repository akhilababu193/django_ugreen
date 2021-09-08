from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import detail

from urbangreen import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('blog.html', views.blog, name='blog'),
    path('blog-detail.html', views.blog1, name='blog-detail'),
    path('about-us.html', views.about, name='about-us'),
    path('cart-page.html', views.cart, name='cart-page'),
    path('contact-us.html', views.contact, name='contact-us'),
    path('shop.html', views.shop, name='shop'),
    path('shop-detail.html', views.shop1, name='shop-detail'),
    path('potting_soil.html', views.potting_soil, name='potting_soil'),
    path('plant_health.html', views.plant_health, name='plant_health'),
    path('seeds.html', views.seeds, name='seeds'),
    path('accessories.html', views.accessories, name='accessories'),
    path('services.html', views.services, name='services'),
    # path('', views.home, name='home'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

