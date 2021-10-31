from django.urls import path
from . import views

urlpatterns = [
        path('as3/', views.show_bansky),
    ]