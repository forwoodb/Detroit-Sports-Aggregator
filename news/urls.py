from django.urls import path 
from .views import *

urlpatterns = [ 
    path('', index),
    path('tigers/', tigers),
    path('lions/', lions),
    path('pistons/', pistons),
    path('redwings/', redwings),
]