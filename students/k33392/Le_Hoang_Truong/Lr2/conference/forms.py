from typing import Any
from django import forms 
import re
from .models import User
from django.core.exceptions import ObjectDoesNotExist

class RegistrationForm(forms.Form) :
    name = forms.CharField(label = 'Name', max_length=30)
    username = forms.CharField(label = 'Username', max_length=30)
    email = forms.EmailField(label = 'Email')
    password1 = forms.CharField(label = 'Password', widget = forms.PasswordInput())
    password2 = forms.CharField(label = 'Password', widget = forms.PasswordInput())

    def clean_password2(self) :
        if 'password1' in self.cleaned_data :
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1 :
                return password2
        raise forms.ValidationError('Password is invalid')
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$',username) :
            raise forms.ValidationError('Username has invalid character')
        try :
            User.objects.get(username=username)
        except ObjectDoesNotExist :
            return username 
        raise forms.ValidationError('Account have already existed')
    
    def save(self) :
        User.objects.create_user(name = self.cleaned_data['name'],username=self.cleaned_data['username'],email = self.cleaned_data['email'],password= self.cleaned_data['password1'])

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["name", "username", "email", "birthday"]
