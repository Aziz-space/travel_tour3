from django.urls import path
from . import views

urlpatterns = [
    path('create-tour/', views.create_tour, name='create_tour'),
    path('update/<int:id>/', views.update_tour, name='update_tour'),
    path('login/', views.login_profile, name='login'),
    path('logout/', views.logout_profile, name='logout'),
    path('delete/<int:id>/', views.delete_tour, name='delete_tour'),
    path('', views.workspace, name='workspace'),
]
