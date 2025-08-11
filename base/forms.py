from django import forms
from base.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title','info','description','category','price']
