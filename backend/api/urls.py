from . import views
from django.urls import path
from .views import api_home

urlpatterns = [
    path('',views.api_home)
]
