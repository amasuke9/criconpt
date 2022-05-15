from django.urls import path
from . import views

urlpatterns = [
    path('', views.ptform, name='ptform'),
]