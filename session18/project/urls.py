from django.contrib import admin
from django.urls import path, include
import board.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', board.views.board, name='board'),
    # board app
    path('board/', include('board.urls')),
    # accounts app
    path('accounts/', include('accounts.urls')),
    # wordcount app
    path('wordcount/', include('wordcount.urls')),
]
