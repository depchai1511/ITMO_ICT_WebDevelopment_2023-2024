# URL 

Мое Django приложение определяет различные URL-пути, которые соответствуют представлениям для обработки HTTP запросов. Вот список URL-путей в приложении:


## Вход (LoginView)

- **URL-шаблон**: `/login/`
- **Представление**: `login`
- **Описание**: Этот путь используется для входа пользователя в систему. Он использует стандартное представление для входа Django.

## Создание конференции

- **URL-шаблон**: `/create/`
- **Представление**: `create_conference`
- **Описание**: Этот путь позволяет пользователям создавать новые конференции.

## Регистрация нового пользователя

- **URL-шаблон**: `/signup/`
- **Представление**: `signup`
- **Описание**: Этот путь используется для регистрации новых пользователей.

## Выход из системы

- **URL-шаблон**: `/logout/`
- **Представление**: `user_logout`
- **Описание**: Этот путь позволяет пользователям выходить из системы.

## Список конференций

- **URL-шаблон**: `/`
- **Представление**: `list_conference`
- **Описание**: Этот путь отображает список всех доступных конференций.

## Подробности о конференции

- **URL-шаблон**: `/<int:id>/`
- **Представление**: `conference`
- **Описание**: Этот путь отображает подробную информацию о конкретной конференции.

## Регистрация на конференцию

- **URL-шаблон**: `/register/<int:conference_id>/`
- **Представление**: `register_conference`
- **Описание**: Этот путь используется для регистрации пользователя на конференцию.

## Отмена регистрации на конференцию

- **URL-шаблон**: `/cancel_registration/<int:conference_id>/`
- **Представление**: `cancel_registration`
- **Описание**: Этот путь позволяет пользователю отменить регистрацию на конференцию.

## Список участников конференции

- **URL-шаблон**: `/participants/<int:id>/`
- **Представление**: `list_participant`
- **Описание**: Этот путь отображает список участников конкретной конференции.

## Результаты и комментарии к конференции

- **URL-шаблон**: `/conference/<int:id>/`
- **Представление**: `conference`
- **Описание**: Этот путь позволяет пользователям просматривать результаты и комментарии к конференции.

## Профиль пользователя

## Профиль пользователя

- **URL-шаблон**: `/profile/`
- **Представление**: `profile`
- **Описание**: Этот путь отображает профиль пользователя и список конференций, в которых он участвует.

## Редактирование профиля пользователя

- **URL-шаблон**: `/profile/<pk>/update/`
- **Представление**: `UserUpdateView`
- **Описание**: Этот путь используется для редактирования профиля пользователя.

Эти URL-пути обеспечивают навигацию и взаимодействие пользователя с веб-приложением Django.

## Реализация

```python
from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    
    path('login/', views.login, name='login'),
    path('create/', views.create_conference, name='create_conference'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.list_conference),
    path('<int:id>/', views.conference,name = 'conference'),
    path('register/<int:conference_id>/', views.register_conference),
    path('cancel_registration/<int:conference_id>/', views.cancel_registration),
    path('participants/<int:id>/', views.list_participant,name ="participants"),
    path('profile/',views.profile,name='profile'),
    path("profile/<pk>/update", views.UserUpdateView.as_view(), name="update_user"),
]

```