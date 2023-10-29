from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Driver(AbstractUser):
    name = models.CharField(max_length=50)
    birthday = models.DateField(null=True)
    passport = models.CharField(max_length=50,  null=True)
    address = models.CharField(max_length=100,  null=True)
    nationality = models.CharField(max_length=30, null=True)
    cars = models.ManyToManyField("Car", through="Ownership", related_name="drivers")

    def __str__(self):
        return self.name

class Car(models.Model) :
    id = models.IntegerField(primary_key=True)
    model = models.CharField(max_length=50)
    label = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.model} {self.label} {self.color}"


class Ownership(models.Model) :
    car = models.ForeignKey("Car", on_delete=models.CASCADE)
    driver = models.ForeignKey("Driver", on_delete=models.CASCADE)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.car.model} {self.driver.name}"

class DriverLicense(models.Model) :
    driver = models.ForeignKey("Driver", on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    creation_date = models.DateField()

    def __str__(self):
        return self.driver.first_name