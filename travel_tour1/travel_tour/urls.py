from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='index'),
    path('tour/<int:id>/', views.detail_tour, name='detail_tour'),
    # Другие URL-шаблоны здесь, если есть
]
