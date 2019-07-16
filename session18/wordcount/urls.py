from django.urls import path
from . import views

urlpatterns = [
    path('count/', views.count, name='count'),
    path('result/', views.result, name='result'),
]