from django.urls import path
from . import views

app_name = 'views'

urlpatterns = [
    path('', views.main, name='main'),
]