#from os import pipe
from django.urls import path
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, urlpatterns

urlpatterns = [
    path('nachoua/',views.func_first,name='func_first')
]
urlpatterns = urlpatterns+staticfiles_urlpatterns()