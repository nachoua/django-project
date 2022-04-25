from django import urls
from django.urls import path
from django.contrib import admin
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

#from django.conf import settings
#from django.conf.urls.static import static
#urls config
urlpatterns = [
    path('hello/',views.say_hello),
    
]
#urlpatterns +=staticfiles_urlpatterns()

