from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('',views.index,name="home"),
    path('login',views.loginuser,name='loginuser'),
    path('logout',views.logoutuser,name='logoutuser'),
    path('printout',views.printout,name='printout'),
    path('redcanteen',views.redcanteen,name='redcanteen'),
    path('restaurant',views.restaurant,name='restaurant'),
    path('yellowcanteen',views.yellowcanteen,name='yellowcanteen'),
    path('signup',views.signup,name='signup'),
    path('register',views.register,name='register'),
    path('profile',views.profile, name='profile'),
    path('contact',views.contact, name='contact'),
]
