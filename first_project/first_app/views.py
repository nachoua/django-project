from django.shortcuts import render
from django.http import  HttpResponseForbidden
from .models import Article
from .models import Login
def article_list(request):
    #articles=Article.objects.all().order_by('date')
    return render(request,'hello.html',#{'articles':articles}
    )
def login_list(request):
   loginn = Login.objects.all([0],[1])
   return render(request,'hello.html',{'loginn':loginn}
    )
    


# Create your views here.
def say_hello(request):
    #return HttpResponse('hello miss nachoua ')
    return render(request,'hello.html')
