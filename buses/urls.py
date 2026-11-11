from django.urls import path
from . import views

urlpatterns = [
    path('add-bus/', views.add_bus, name='add_bus'),
    path('bus/<int:bus_id>/seats/', views.bus_seat_layout, name='bus_seat_layout'),
]
