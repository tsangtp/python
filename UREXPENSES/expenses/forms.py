from django import forms
from .models import Expense
class ExpenseModelForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = {
            'name',
            'price',
            'image',
        }
        labels = {
            'image': 'Image',
            'name': 'Product Name',
            'price': 'Price'
        }
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control-file'})
        }