from django.urls import path,include
from . import views
app_name = 'users'
urlpatterns = [
    #Включить URL авторизации по умолчанию.
    path('register/', views.register, name='register'),
]