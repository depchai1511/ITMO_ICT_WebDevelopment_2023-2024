from django.shortcuts import render
from .models import Car,Driver
from django.http import Http404
from .forms import DriverUpdateForm, DriverCreateForm,CarCreateForm,CarUpdateForm
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView,
)

def index(request) :
    return render(request, "pages/home.html")

def driver(request,id): 
    try: 
        p = Driver.objects.get(id=id)  
    except Driver.DoesNotExist:
        raise Http404("Driver does not exist") 
    return render(request, 'pages/driver.html', {'driver': p}) 

def alldrivers(request):
    drivers  = Driver.objects.all()
    return render(request, 'pages/drivers.html', {'drivers': drivers})

class driverView(DetailView):
    model = Driver
    template_name = "pages/driver.html"
    context_object_name = "driver"

class CarListView(ListView):
    model = Car
    template_name = "pages/cars.html"
    context_object_name = "cars"


class DriverListView(ListView):
    model = Driver
    template_name = "pages/drivers.html"
    context_object_name = "drivers"


class DriverCreateView(CreateView):
    model = Driver
    template_name = "pages/create_driver.html"
    form_class = DriverCreateForm
    success_url = "/drivers"


class DriverUpdateView(UpdateView):
    model = Driver
    template_name = "pages/update_driver.html"
    form_class = DriverUpdateForm
    success_url = "/drivers"

class DriverDeleteView(DeleteView):
    model = Driver
    template_name = "pages/delete_driver.html"
    success_url = "/drivers"
    
class CarCreateView(CreateView):
    model = Car
    template_name = "pages/create_car.html"
    form_class = CarCreateForm
    success_url = "/cars"


class CarUpdateView(UpdateView):
    model = Car
    template_name = "pages/update_car.html"
    form_class = CarUpdateForm
    success_url = "/cars"


