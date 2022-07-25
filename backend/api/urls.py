from . import views
from django.urls import path
from .views import api_home
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('',views.api_home),
    path('auth/',obtain_auth_token)
]
