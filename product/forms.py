from django import forms
from .models import products
class ProductForm(forms.ModelForm):
    class Meta:
        model=products
        fields=['image','name','category','price','description']
        widgets={
            'image':forms.FileInput(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'category' : forms.Select(attrs={'class':'form-control'}),
            'price':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.TextInput(attrs={'class':'form-control'}),  
        }
    