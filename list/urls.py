from django.contrib import admin
from django.urls import path, include

from .views import ListView

urlpatterns = [
    path('', ListView.as_view(), name="list"),
]
