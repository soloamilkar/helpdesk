from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('create/', views.create_user, name='create'),
    path('detail/', views.create_user, name='detail'),
    path('rol/', views.user_rol, name='rol'),
]