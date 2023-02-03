from django.urls import path
from .views import *



urlpatterns = [
    path('', home),
    path('formations/', formations),
    path('formations/<int:pk>/', formation),
]
