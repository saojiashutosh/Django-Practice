from django.shortcuts import render,redirect
from django.http import *
from .models import user
from .forms import UserForm ,SigninForm,BlogForm
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
        if form.is_valid():  # Validate the form
            print("Form is valid")
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            try:
                # Get user by username
                obj = user.objects.get(username=username)
                print("User found")

                # Check if password matches
                if check_password(password, obj.password):
                    print("Password match!")
                    return HttpResponse(f"Welcome {username}")
                else:
                    print("Invalid password!")
                    form.add_error('password', "Invalid password.")
            except user.DoesNotExist:
                form.add_error('username', "Username does not exist.")  # User not found
        else:
            print("Form is invalid")
    else:
        form = SigninForm()

    return render(request, "app/signin.html", {'form': form})

def blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)

    form = BlogForm()
    return render(request,"app/blog.html",{'form':form})
