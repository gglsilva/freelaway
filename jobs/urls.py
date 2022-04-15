from django.urls import path
from .views import *


urlpatterns = [
    path('encontrar_jobs/', encontrar_jobs, name='encontrar_jobs'),
]