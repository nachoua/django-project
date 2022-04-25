from django.http import request
#from form_login.forms import LoginForm
from django.shortcuts import render,redirect
from .models import Login
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login

# Create your views here
def func_login(request):
    if request.method =='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
           # user=form.get_user()#user in
            #login(request,user)#user in()
            return redirect('logoutt')
    else:

        form=AuthenticationForm()
    return render(request,'fichier_html.html',{'form':form})

def func_page(request):
    # form=LoginForm()
    # context={'form':form}
    if request.method =='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
           form.save()
        return redirect('logoutt')
    else:
        
        form=UserCreationForm()
    return render(request,'page.html',{'form':form})

def func_logout(request):
    #form=LoginForm()
    #context={'form':form}
    return render(request,'logout.html')

# def func_sign(request):
    form=LoginForm()
    context={'form':form}
    # return render(request,'Sign_Up.html')
def func_pp(request):
    # form=LoginForm()
    # context={'form':form}
     return render(request,'pp.html')
# 
def login_page(request): 

    # if request.method == 'POST':
    # context = {}
    return render(request,'page.html')#context
# """ def test(request): """
# """     if request.method == 'POST """':
# """         request.POST.get('user """nam')
# """         request.POST.get('pass """word')
# """     context = {} """
# """     return render(request, 'pa """ge.html',context)
# """ def authenticationn(request): """
# """  """
# """     usernam = request.POST['us """ername']
# """     password = request.POST['p """assword']
# """     Login = authenticate(reque """st, usernam=usernam, password=password)
# """     if Login is not None: """
# """         login(request, Login) """
# """         print("Redirect to a s """uccess page")
# """     else: """
# """         print("invalid login") """









    