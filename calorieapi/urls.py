from django.urls import path
from . import views

urlpatterns = [
    path('api/calories', views.get_calories, name='get_calories'),
]
