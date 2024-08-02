from django import forms
from travel_tour.models import Category, Tag, Tour
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User


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
        
        
        
        
        
class LoginForm(forms.Form):

    username = forms.CharField(
        widget=forms.TextInput(attrs={"autofocus": True, 'class': 'form-control', 'placeholder': 'имя пользователя'}), 
        label='Имя пользователя'
    )
    password = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", 'class': 'form-control', 'placeholder': 'пароль'}),
    )  
    
    









class RegisterForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True 
        self.fields['last_name'].required = True 
        self.fields['email'].required = True 

    password1 = forms.CharField(label='Придумайте пароль', validators=[validate_password], widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))

    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email')
        
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            self.add_error('password2', "The passwords don't match.")
        
        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user