from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from travel_tour.models import Tour, Category, Tag
from .forms import *


def workspace(request):
    tours = Tour.objects.all()
    page = int(request.GET.get('page', 1))
    page_size = int(request.GET.get('page_size', 4))
 
    paginator = Paginator(tours, page_size)
    page_obj = paginator.get_page(page) 

    return render(request, 'workspace/index.html', {'page_obj': page_obj})

def create_tour(request):
    form = TourForm()

    if request.method == 'POST':
        form = TourForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            news = form.save()
            return redirect('/workspace/')
         
    return render(request, 'workspace/create_tour.html', {'form': form})

def delete_tour(request, id):
    tour = get_object_or_404(Tour, id=id)
    tour.delete()
    return redirect('/workspace/')


# fdsjafjkldsklfjkldskfjdklfkdsj


def update_tour(request, id):
    tour = get_object_or_404(Tour, id=id)
    form = TourForm(instance=tour)
    if request.method == 'POST':
        form = TourForm(data=request.POST, files=request.FILES, instance=tour)
        if form.is_valid():
            form.save()
            return redirect('/workspace/')
                
    return render(request, 'workspace/update_tour.html', {'form': form, 'tour': tour})

