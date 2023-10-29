from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50,unique=True)
    birthday = models.DateField(null=True)
    passport = models.CharField(max_length=50,  null=True)
    address = models.CharField(max_length=100,  null=True)
    nationality = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Conference(models.Model):

    name = models.CharField(max_length=50)
    decription = models.CharField(max_length=500)
    start_date = models.DateField(auto_now=False, auto_now_add=True)
    end_date = models.DateField(auto_now=True, auto_now_add=False)
    location = models.CharField(max_length=50)
    topics = models.ManyToManyField(
        "Topic", through="ConferenceTopic", related_name="conferences")
    result = models.IntegerField(
        validators=[
            MinValueValidator(1, message='The value must greater than 1.'),
            MaxValueValidator(10, message='The value must smaller than 10.'),
        ]
    ,default = 10)
    recommended = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ConferenceTopic(models.Model):
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)


class Registration(models.Model):
    creation_date = models.DateField(auto_now=False, auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name + " registers for conference '" + self.conference.name + "'"

class Comment(models.Model):
    creation_date = models.DateField(auto_now=False, auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1, message='The value must greater than 1.'),
            MaxValueValidator(10, message='The value must smaller than 10.'),
        ]
    ,null=True)
    content = models.CharField(max_length=500)

    def __str__(self):
        return self.user.name 


class PresentationResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="presentation_results")
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE, related_name="presentation_results")
