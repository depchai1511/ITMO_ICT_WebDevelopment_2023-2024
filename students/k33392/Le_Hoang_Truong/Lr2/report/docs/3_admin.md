# Admin

Ниже приведены зарегистрированные модели для использования в админ-панели Django.

## Зарегистрированные модели:

- **Пользователь (User)**: `admin.site.register(User)`
- **Конференция (Conference)**: `admin.site.register(Conference)`
- **Тема конференции (ConferenceTopic)**: `admin.site.register(ConferenceTopic)`
- **Тема (Topic)**: `admin.site.register(Topic)`
- **Регистрация (Registration)**: `admin.site.register(Registration)`
- **Комментарий (Comment)**: `admin.site.register(Comment)`
- **Результат презентации (PresentationResult)**: `admin.site.register(PresentationResult)`

Эти модели зарегистрированы для управления через административную панель Django.


## Реализация

```python
from django.contrib import admin
from .models import User,Conference,ConferenceTopic,Topic,Registration,Comment,PresentationResult


# Register your models here.
admin.site.register(User)
admin.site.register(Conference)
admin.site.register(ConferenceTopic)
admin.site.register(Topic)
admin.site.register(Registration)
admin.site.register(Comment)
admin.site.register(PresentationResult)

```