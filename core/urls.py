from django.urls import path
from .views import CreatePromo, ActivatePromo, CheckPromo
urlpatterns = [
    path('create', CreatePromo.as_view()), 
    path('activate', ActivatePromo.as_view()), 
    path('check/', CheckPromo.as_view()), 
]

