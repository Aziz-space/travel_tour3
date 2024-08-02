from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from travel_tour.models import Tour, Category, Tag
from .forms import *
from pprint import pprint
from workspace.forms import LoginForm,  RegisterForm
from django.contrib.auth import authenticate, login, logout


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





def update_tour(request, id):
    tour = get_object_or_404(Tour, id=id)
    form = TourForm(instance=tour)
    if request.method == 'POST':
        form = TourForm(data=request.POST, files=request.FILES, instance=tour)
        if form.is_valid():
            form.save()
            return redirect('/workspace/')
                
    return render(request, 'workspace/update_tour.html', {'form': form, 'tour': tour})









def login_profile(request):
    if request.user.is_authenticated:
        return redirect('/workspace/')
    
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)   
                return redirect('/workspace/') 
            

            message = 'The user does not exist or the password is incorrect.'
            return render(request, 'auth/login.html', {'form': form, 'message': message})


    return render(request, 'auth/login.html', {'form': form})


def logout_profile(request):
    if request.user.is_authenticated:
        logout(request)
    
    return redirect('/workspace/')











def register_profile(request):
    if request.user.is_authenticated:
        return redirect('/workspace/')
    
    form = RegisterForm()

    
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/workspace/')
    

    return render(request, 'auth/register.html', {'form': form})