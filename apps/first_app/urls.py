from django.urls import path
from . import views

urlpatterns = [ 
        path('hello/', views.hello),
        path('crudrops/', views.crudops),
        path('as3/', views.show_bansky),
    ]