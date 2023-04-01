from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('list/', views.meal_list),
    path('details/<int:pk>/', views.meal_detail),
]
