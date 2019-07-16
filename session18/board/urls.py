from django.urls import path
from . import views

urlpatterns = [
    path('<int:board_id>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('boardpost/', views.boardpost, name='boardpost'),
]