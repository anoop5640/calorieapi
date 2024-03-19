from django.urls import path
from .views import FoodCalorieView

urlpatterns = [
    path('calories/<str:name>/', FoodCalorieView.as_view(), name='food-calorie'),
]
