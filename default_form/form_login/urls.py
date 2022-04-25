from os import pipe
from django import urls
from django.urls import path
from django.contrib import admin
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, urlpatterns
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('nachoua/',views.func_login,name="nachoua_login"),
    path('page/',views.func_page,name="pagee"),
    path('logout/',views.func_logout,name="logoutt"),
    #path('sign_up/',views.func_sign,name="sign"),
    #path('test/',views.test,name="test"),
    path('login_page/',views.login_page,name="login_page"),
    #path('authenticationn/',views.authenticationn,name="authenticationn"),
    path('pp/',views.func_pp,name="ppp")
]

urlpatterns = urlpatterns+staticfiles_urlpatterns()