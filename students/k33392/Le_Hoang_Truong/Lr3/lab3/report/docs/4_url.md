# URL

Это приложение Django определяет различные URL-пути для обработки HTTP-запросов, связанных с управлением автобусами. Шаблоны URL организованы с использованием функции `path` Django и `DefaultRouter` из модуля `rest_framework.routers`.

## API-точки

### Водители

- **Список и Создание Водителей**: `/drivers/`
- **Получение, Обновление и Удаление Водителя**: `/drivers/<int:pk>/`

### Автобусы

- **Список и Создание Автобусов**: `/buses/`
- **Получение, Обновление и Удаление Автобуса**: `/buses/<int:pk>/`

### Типы Автобусов

- **Список и Создание Типов Автобусов**: `/bus-types/`
- **Получение, Обновление и Удаление Типа Автобуса**: `/bus-types/<int:pk>/`

### Маршруты

- **Список и Создание Маршрутов**: `/routes/`
- **Получение, Обновление и Удаление Маршрута**: `/routes/<int:pk>/`
- **Список Водителей на Маршруте**: `/routes/<int:route_id>/drivers/` (Пользовательское представление)
- **Расписание Автобусов по Маршруту**: `/routes/<int:route_id>/schedule/` (Пользовательское представление)

### Назначения

- **Список и Создание Назначений**: `/assignments/`
- **Получение, Обновление и Удаление Назначения**: `/assignments/<int:pk>/`

### Поломки

- **Список и Создание Поломок**: `/breakdowns/`
- **Получение, Обновление и Удаление Поломки**: `/breakdowns/<int:pk>/`
- **Неактивные Автобусы на Дату**: `/breakdowns/<str:date>/inactive-buses/` (Пользовательское представление)

### Статистика Водителей

- **Количество Водителей по Классу**: `/drivers/class/<str:class_name>/` (Пользовательское представление)

### URL-адреса аутентификации по умолчанию
- **Шаблон URL:** `re_path(r"^auth/", include("djoser.urls"))`
- **Описание:** Включает URL-адреса аутентификации по умолчанию, предоставленные DJoser.
- **Использование:**
    - `/auth/users/`: Операции CRUD для учетных записей пользователей.
    - `/auth/users/me/`: Получение или обновление профиля текущего пользователя.
    - `/auth/users/activation/`: Активация учетной записи пользователя.
    - `/auth/users/resend_activation/`: Повторная отправка электронного письма с активацией.
    - `/auth/password/reset/`: Запрос сброса пароля.
    - `/auth/password/reset/confirm/`: Подтверждение сброса пароля.
    - `/auth/password/set/`: Установка нового пароля пользователя.
    - `/auth/password/set/confirm/`: Подтверждение установки нового пароля пользователя.
    - `/auth/token/login/`: Получение токена аутентификации.
    - `/auth/token/logout/`: Выход из системы и аннулирование токена аутентификации.

### URL-адреса аутентификации с токеном
- **Шаблон URL:** `re_path(r"^auth/", include("djoser.urls.authtoken"))`
- **Описание:** Включает URL-адреса аутентификации для токен-аутентификации, предоставленные DJoser.
- **Использование:**
    - `/auth/token/login/`: Получение токена аутентификации.
    - `/auth/token/logout/`: Выход из системы и аннулирование токена аутентификации.
    - `/auth/token/refresh/`: Обновление существующего токена аутентификации.

## Реализация

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    DriverViewSet,
    BusViewSet,
    BusTypeViewSet,
    RouteViewSet,
    AssignmentViewSet,
    BreakdownViewSet,
    DriversOnRouteView,
    BusScheduleView,
    InactiveBusesView,
    DriverCountByClassView,
)

router = DefaultRouter()
router.register(r'drivers', DriverViewSet)
router.register(r'buses', BusViewSet)
router.register(r'bus-types', BusTypeViewSet)
router.register(r'routes', RouteViewSet)
router.register(r'assignments', AssignmentViewSet)
router.register(r'breakdowns', BreakdownViewSet)

urlpatterns = [
    path('routes/<int:route_id>/drivers/', DriversOnRouteView.as_view(), name='drivers-on-route'),
    path('routes/<int:route_id>/schedule/', BusScheduleView.as_view(), name='bus-schedule'),
    path('breakdowns/<str:date>/inactive-buses/', InactiveBusesView.as_view(), name='inactive-buses'),
    path('drivers/class/<str:class_name>/', DriverCountByClassView.as_view(), name='driver-count-by-class'),
]

urlpatterns += router.urls
```