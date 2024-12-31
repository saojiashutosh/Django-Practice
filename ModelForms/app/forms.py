from django.forms import ModelForm
from .models import user

class UserForm(ModelForm):
    class Meta:
        model = user
        fields = "__all__"

class SigninForm(ModelForm):
    class Meta:
        model = user
        fields = ["username","password"]