from django.shortcuts import render,redirect
from django.http import *
from .models import user
from .models import blog
from .forms import UserForm ,SigninForm,BlogForm
from django.contrib.auth.hashers import make_password,check_password
 
# Create your views here.
def home(request):
    data = user.objects.all()
    blogs = blog.objects.all()
    word = "Blogs for You"
    return render(request, "app/index.html", {'data': data, 'word': word, 'blogs': blogs})


# this is user registration view
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
            request.session['username']=username
            return redirect("/")
        else:
             form.add_error("An error Occured during Signup")
        

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
                    request.session['username']=username
                    return redirect("/")
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

def logout(request):
    request.session.flush()
    print("Session cleared:", request.session.items())
    return redirect('Signin')
# end of registration

def blogPage(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            if request.session.get('username'):
                username = request.session.get('username')
                user_obj = user.objects.get(username=username)
                obj = blog(title = title,content = content,name = user_obj)
                obj.save()

                return redirect('/')
            else:
                form.add_error(None, "You have to Signin First to Post the blog")
                print("Error added to form:", form.errors) 

    form = BlogForm()
    return render(request,"app/blog.html",{'form':form})


def details(request):
    username = request.session.get('username')
    obj = user.objects.get(username = username)
    no_blogs = blog.objects.filter(name=obj).count()

    return render(request,"app/details.html",{'obj':obj,'no_blogs':no_blogs})