from django.urls import path
from .views import index, getData


urlpatterns = [
    
    path('index/', index),
    path('getData/', getData, name = "getData")
]