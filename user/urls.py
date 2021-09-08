from django.urls import path
from urbangreen import views

urlpatterns = [
    path('register', views.user_register),
    path('login', views.user_login),

]
