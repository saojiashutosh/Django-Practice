from django import forms
from django.forms import ModelForm
from .models import user,blog

class UserForm(ModelForm):
    class Meta:
        model = user
        fields = "__all__"

class SigninForm(forms.Form):
    username = forms.CharField(label="Username", max_length=10)
    password = forms.CharField(label="Password", max_length=16)

class BlogForm(forms.ModelForm):
    class Meta:
        model = blog
        fields = ['title', 'content']
        labels = {'title':'Blog Title',
                  'content':'Enter Blog Content'}
    