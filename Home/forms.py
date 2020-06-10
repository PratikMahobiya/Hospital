from django import forms
from .models import User


class user_Form(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"

class login_form(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)