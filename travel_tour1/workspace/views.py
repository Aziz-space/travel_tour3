from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.urls import reverse
from travel_tour.models import Tour
from .forms import TourForm
from workspace.forms import LoginForm, RegisterForm, ChangePsswordForm, ChangeProfileForm
from django.contrib.auth import authenticate, login, logout
from .decorators import admin_required
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def workspace(request):
    tours = Tour.objects.all()
    page = int(request.GET.get('page', 1))
    page_size = int(request.GET.get('page_size', 4))
    
    paginator = Paginator(tours, page_size)
    page_obj = paginator.get_page(page)
    
    return render(request, 'workspace/index.html', {'page_obj': page_obj})

@admin_required
def create_tour(request):
    form = TourForm()

    if request.method == 'POST':
        form = TourForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            tour = form.save()
            messages.success(request, f'Тур "{tour.name}" добавлен')
            return redirect(reverse('workspace'))
        else:
            return render(request, 'workspace/create_tour.html', {'form': form})

    return render(request, 'workspace/create_tour.html', {'form': form})

@admin_required
def delete_tour(request, id):
    tour = get_object_or_404(Tour, id=id)
    tour.delete()
    messages.success(request, f'Тур "{tour.name}" удален') 
    return redirect(reverse('workspace'))

@admin_required
def update_tour(request, id):
    tour = get_object_or_404(Tour, id=id)
    form = TourForm(instance=tour)
    
    if request.method == 'POST':
        form = TourForm(data=request.POST, files=request.FILES, instance=tour)
        if form.is_valid():
            form.save()
            messages.success(request, f'Тур "{tour.name}" обнавлен')
            return redirect(reverse('workspace'))
        else:
            # Обработка ошибок
            return render(request, 'workspace/update_tour.html', {'form': form, 'tour': tour})

    return render(request, 'workspace/update_tour.html', {'form': form, 'tour': tour})

def login_profile(request):
    if request.user.is_authenticated:
        return redirect(reverse('workspace'))

    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Вы успешно вошли в систему.')
                return redirect(reverse('workspace'))
            else:
                messages.error(request, 'Неверное имя пользователя или пароль.')
        else:
            messages.error(request, 'Исправьте ошибки в форме.')

    return render(request, 'auth/login.html', {'form': form})

def logout_profile(request):
    if request.user.is_authenticated:
        logout(request)
    
    messages.success(request, f'До свидания!')
    
    return redirect(reverse('workspace'))

def register_profile(request):
    if request.user.is_authenticated:
        return redirect(reverse('workspace'))
    
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Добро пожаловать "{user.get_full_name()}"')
            return redirect(reverse('workspace'))

        messages.error(request, f'Исправьте некоторые ошибки, приведенные ниже!')

    return render(request, 'auth/register.html', {'form': form})















@login_required(login_url='/workspace/login/')
def profile(request):

    form = ChangeProfileForm(instance=request.user)

    if request.method == 'POST':
        form = ChangeProfileForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Профиль успешно изменен')
            return redirect('/workspace/')

    return render(request, 'auth/profile.html', {'form': form})


@login_required(login_url='/workspace/login/')
def change_password(request):

    form = ChangePsswordForm(user=request.user)

    if request.method == 'POST':

        form = ChangePsswordForm(user=request.user, data=request.POST)

        if form.is_valid():
            new_password = form.cleaned_data.get('new_password')
            
            user = request.user
            user.set_password(new_password)
            user.save()

            login(request, user)

            messages.success(request, f'Пароль успешно обновлен')
            return redirect('/workspace/')

    return render(request, 'auth/change_password.html', {'form': form})
