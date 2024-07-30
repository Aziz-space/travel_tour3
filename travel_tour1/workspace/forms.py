from django import forms
from travel_tour.models import Category, Tag, Tour


class TourForm(forms.ModelForm):

    class Meta:
        model = Tour
        fields = (
            'name',
            'image',
            'price',
            'description',
            'location',
            'category',
            'tags',
        )

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название',
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'cols': '5',
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'tags': forms.CheckboxSelectMultiple(),
            'category': forms.Select(attrs={
                'class': 'form-select',
            }),
        }
        
        
        
        
class UpdateForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = (
            'name',
            'image',
            'price',
            'description',
            'location',
            'category',
            'tags',
        )        
        
        
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название',
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'cols': '5',
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'tags': forms.CheckboxSelectMultiple(),
            'category': forms.Select(attrs={
                'class': 'form-select',
            }),
        }