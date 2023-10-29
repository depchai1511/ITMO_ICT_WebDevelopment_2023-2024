# Model

## Модель User

Модель User представляет собой пользователей вашего веб-приложения. Она наследуется от `AbstractUser` и содержит следующие поля:

- `name` (имя) - поле для имени пользователя.
- `username` (имя пользователя) - уникальное поле для имени пользователя.
- `birthday` (дата рождения) - поле для даты рождения пользователя.
- `passport` (паспорт) - поле для информации о паспорте пользователя.
- `address` (адрес) - поле для адреса пользователя.
- `nationality` (национальность) - поле для национальности пользователя.

## Модель Topic

Модель Topic представляет собой темы или тематики конференций. Она содержит следующее поле:

- `name` (название) - поле для названия темы.

## Модель Conference

Модель Conference представляет собой информацию о конференциях. Она содержит следующие поля:

- `name` (название) - поле для названия конференции.
- `description` (описание) - поле для описания конференции.
- `start_date` (дата начала) - поле для даты начала конференции.
- `end_date` (дата окончания) - поле для даты окончания конференции.
- `location` (местоположение) - поле для указания места проведения конференции.
- `topics` (темы) - множественное поле для связи с моделью Topic.
- `result` (результат) - поле для результата презентации на конференции.
- `recommended` (рекомендовано) - поле для указания, рекомендован ли пользователь для публикации.

## Модель ConferenceTopic

Модель ConferenceTopic представляет связь между конференциями и их темами. Она содержит следующие поля:

- `conference` (конференция) - внешний ключ для связи с моделью Conference.
- `topic` (тема) - внешний ключ для связи с моделью Topic.

## Модель Registration

Модель Registration представляет регистрацию пользователей на конференции. Она содержит следующие поля:

- `creation_date` (дата создания) - поле для даты создания записи регистрации.
- `user` (пользователь) - внешний ключ для связи с моделью User.
- `conference` (конференция) - внешний ключ для связи с моделью Conference.

## Модель Comment

Модель Comment представляет комментарии пользователей к конференциям. Она содержит следующие поля:

- `creation_date` (дата создания) - поле для даты создания комментария.
- `user` (пользователь) - внешний ключ для связи с моделью User.
- `conference` (конференция) - внешний ключ для связи с моделью Conference.
- `rating` (рейтинг) - поле для рейтинга комментария (от 1 до 10).
- `content` (содержание) - поле для текста комментария.

## Модель PresentationResult

Модель PresentationResult представляет результаты презентации пользователей на конференциях. Она содержит следующие поля:

- `user` (пользователь) - внешний ключ для связи с моделью User.
- `conference` (конференция) - внешний ключ для связи с моделью Conference.

## Реализация

```python
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

```