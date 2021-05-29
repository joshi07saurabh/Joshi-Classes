from django.contrib import admin
from django.urls import path
from JoshiClasses import views

urlpatterns = [
    path('',views.home,name="home"),
    
]