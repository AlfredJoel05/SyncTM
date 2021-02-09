from django.contrib import admin
from django.urls import path
from .views import detailsPage_view, landingPage_view

urlpatterns = [
    path('', landingPage_view, name = 'landingpage'),
    path('details', detailsPage_view, name = 'detailspage'),
]