from django import forms
from .models import Car, Driver


class DriverCreateForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ["username", "password", "name", "birthday"]



class DriverUpdateForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ["username", "password", "name", "birthday"]



class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [ "label", "model", "color"]
      


class CarUpdateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ["id", "label", "model", "color"]
        