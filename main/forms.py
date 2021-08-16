from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import *
class AddCattle(forms.ModelForm):
    class Meta:
        model = Cattle
        fields = ("__all__")
        '''widget = {
            "buyer": forms.TextInput(attrs={"placeholder":"buyer"}),
            "salesorder": forms.TextInput(attrs={"class":"form-control"}),
            "cattleid": forms.TextInput(attrs={"class":"form-control"}),
            "slaughterorder": forms.TextInput(attrs={"class":"form-control"}),
            "phonenumber": forms.TextInput(attrs={"class":"form-control"})
            

        }'''