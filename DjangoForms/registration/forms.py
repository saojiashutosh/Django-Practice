from django import forms

class UserForms(forms.Form):
    name = forms.CharField(label='Name :',max_length=50)
    contact = forms.CharField(label='Contact :',max_length=11)
    email = forms.EmailField(label='Email :',max_length=254)
    password = forms.CharField(label='Password :',max_length=50)