from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("drivers/", views.alldrivers, name="drivers"),
    path("cars/", views.CarListView.as_view(), name="cars"),
    path("driver/<int:id>", views.driverView.as_view(), name="driver"),
    path("driver/create/", views.DriverCreateView.as_view(), name="create_driver"),
    path("car/create/", views.CarCreateView.as_view(), name="create_car"),
    path("driver/<pk>/update", views.DriverUpdateView.as_view(), name="update_driver"),
    path("driver/<pk>/delete", views.DriverDeleteView.as_view(), name="delete_driver"),
    path("car/<pk>/update", views.CarUpdateView.as_view(), name="update_driver"),
    path("driver/<pk>/delete", views.DriverDeleteView.as_view(), name="delete_driver"),
]