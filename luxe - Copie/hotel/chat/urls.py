from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat, name='chat'),
      # Add a new URL pattern for the combined charts
]
