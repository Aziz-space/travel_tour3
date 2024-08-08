import django_filters
from travel_tour.models import Category, Tour, Tag
from django import forms

class TourFilter(django_filters.FilterSet):
    categories = django_filters.ModelMultipleChoiceFilter(
        field_name='category',
        queryset=Category.objects.all(),
        label='Категории',
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'filter-checkbox'
        })
    )
    tags = django_filters.ModelMultipleChoiceFilter(
        field_name='tags',
        queryset=Tag.objects.all(),
        label='Теги',
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'filter-checkbox'
        })
    )
    
    class Meta:
        model = Tour
        fields = ['tags', 'categories']
