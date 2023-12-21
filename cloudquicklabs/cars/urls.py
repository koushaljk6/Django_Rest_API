from django.urls import path
from .views import CarsViewset


urlpatterns = [
    path('cars/', CarsViewset.as_view()),
    path('cars/<str:id>', CarsViewset.as_view())
]