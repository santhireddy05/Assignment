from django.db.models import fields
from .models import Address_Book
from django import forms

class Address_BookForm(forms.ModelForm):
    class Meta:
        model = Address_Book
        fields = ['Name','Email','DOB','Address','Pincode']
