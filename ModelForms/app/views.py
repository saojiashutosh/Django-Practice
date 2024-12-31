from django.shortcuts import render,redirect
from django.http import *
from .models import user
from .forms import UserForm ,SigninForm
from django.contrib.auth.hashers import make_password,check_password
 
# Create your views here.

def home(request):
    data = user.objects.all()
    word = "Hello"
    return render(request,"app/index.html",{'data':data ,'word':word})


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST,request.FILES)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            name = form.cleaned_data.get('name')
            contact = form.cleaned_data.get('contact')
            image = form.cleaned_data.get('image')

            hashed_password = make_password(password)

            obj = user(username=username,name=name, contact=contact, password=hashed_password ,image = image)
            obj.save()

            return redirect("/")
        else:
             return HttpResponse("Ooops ! An Error Occured !!!")
        

    form = UserForm()
    return render(request,"app/signup.html",{'form':form})
        

def signin(request):
    if request.method == "POST":
        form = SigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            obj = user.objects.filter(username)
            if 

    form = SigninForm()
    return render(request,"app/signin.html",{'form':form})
