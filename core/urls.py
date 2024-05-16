from django.urls import path
from .views import createPromo, activatePromo
urlpatterns = [
    path('create', createPromo), 
    path('activate', activatePromo)
]

