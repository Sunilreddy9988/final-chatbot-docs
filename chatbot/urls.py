from django.urls import path
from .views import chatbot, chatbot_ajax, index, getData


urlpatterns = [
    
    path('index/', index),
    path('getData/', getData, name = "getData")
]