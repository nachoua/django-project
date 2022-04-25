from django.shortcuts import render
from django.http import request
from .models import First


# Create your views here.
def  func_first(request):
    projects = First.objects.all().order_by('date')
    return render(request,'fichierhtml.html',{'projects':projects})