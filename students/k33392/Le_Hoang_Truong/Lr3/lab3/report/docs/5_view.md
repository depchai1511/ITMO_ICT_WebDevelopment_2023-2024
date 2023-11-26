# View

## Наборы представлений (ViewSets)
### DriverViewSet
- **Описание:** Обрабатывает операции CRUD для объектов Driver.
- **Сериализатор:** DriverSerializer
- **Queryset:** Все объекты Driver
- **Права доступа:** Ограничены для администраторов (`IsAdminUser`)
- **URL-шаблон**: `/drivers/` и `/drivers/<int:pk>/`

### BusViewSet
- **Описание:** Обрабатывает операции CRUD для объектов Bus.
- **Сериализатор:** BusSerializer
- **Queryset:** Все объекты Bus
- **Права доступа:** Ограничены для администраторов (`IsAdminUser`)
- **URL-шаблон**: `/buses/` и `/buses/<int:pk>/`

### BusTypeViewSet
- **Описание:** Обрабатывает операции CRUD для объектов BusType.
- **Сериализатор:** BusTypeSerializer
- **Queryset:** Все объекты BusType
- **Права доступа:** Ограничены для администраторов (`IsAdminUser`)
- **URL-шаблон**: `/bus-types/` и `/bus-types/<int:pk>/`

### RouteViewSet
- **Описание:** Обрабатывает операции CRUD для объектов Route.
- **Сериализатор:** RouteSerializer
- **Queryset:** Все объекты Route
- **Права доступа:** Ограничены для администраторов (`IsAdminUser`)
- **URL-шаблон**: `/routes/` и `/routes/<int:pk>/`

### AssignmentViewSet
- **Описание:** Обрабатывает операции CRUD для объектов Assignment.
- **Сериализатор:** AssignmentSerializer
- **Queryset:** Все объекты Assignment
- **Права доступа:** Ограничены для администраторов (`IsAdminUser`)
- **URL-шаблон**: `/assignments/` и `/assignments/<int:pk>/`

### BreakdownViewSet
- **Описание:** Обрабатывает операции CRUD для объектов Breakdown.
- **Сериализатор:** BreakdownSerializer
- **Queryset:** Все объекты Breakdown
- **Права доступа:** Ограничены для администраторов (`IsAdminUser`)
- **URL-шаблон**: `/breakdowns/` и `/breakdowns/<int:pk>/`

## Пользовательские представления списка (Custom List Views)
### DriversOnRouteView
- **Описание:** Перечисляет все назначения (водители) для определенного маршрута.
- **Сериализатор:** AssignmentSerializer
- **Queryset:** Фильтровано по route_id из аргументов URL.
- **URL-шаблон**: `routes/<int:route_id>/driver/`

### BusScheduleView
- **Описание:** Перечисляет все назначения (автобусы) для определенного маршрута.
- **Сериализатор:** AssignmentSerializer
- **Queryset:** Фильтровано по route_id из аргументов URL.
- **URL-шаблон**: `routes/<int:route_id>/schedule/`

### InactiveBusesView
- **Описание:** Перечисляет все поломки (неактивные автобусы) для определенной даты.
- **Сериализатор:** BreakdownSerializer
- **Queryset:** Фильтровано по дате из аргументов URL.
- **URL-шаблон**: `/breakdowns/<str:date>/inactive-buses/`

### DriverCountByClassView
- **Описание:** Перечисляет всех водителей, отфильтрованных по их классу.
- **Сериализатор:** DriverSerializer
- **Queryset:** Фильтровано по class_name из аргументов URL.
- **URL-шаблон**: `/drivers/class/<str:class_name>/`

## Реализация

```python
from .serializers import DriverSerializer, BusSerializer, BusTypeSerializer, RouteSerializer, AssignmentSerializer, BreakdownSerializer
from .models import Driver, Bus, BusType, Route, Assignment, Breakdown
from rest_framework import generics,viewsets
from rest_framework.permissions import IsAdminUser

class DriverViewSet(viewsets.ModelViewSet):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()
    permission_classes = [IsAdminUser]

class BusViewSet(viewsets.ModelViewSet):
    serializer_class = BusSerializer
    queryset = Bus.objects.all()
    permission_classes = [IsAdminUser]

class BusTypeViewSet(viewsets.ModelViewSet):
    serializer_class = BusTypeSerializer
    queryset = BusType.objects.all()
    permission_classes = [IsAdminUser]

class RouteViewSet(viewsets.ModelViewSet):
    serializer_class = RouteSerializer
    queryset = Route.objects.all()
    permission_classes = [IsAdminUser]

class AssignmentViewSet(viewsets.ModelViewSet):
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()
    permission_classes = [IsAdminUser]

class BreakdownViewSet(viewsets.ModelViewSet):
    serializer_class = BreakdownSerializer
    queryset = Breakdown.objects.all()
    permission_classes = [IsAdminUser]


class DriversOnRouteView(generics.ListAPIView):
    serializer_class = AssignmentSerializer

    def get_queryset(self):
        route_id = self.kwargs['route_id'] 
        return Assignment.objects.filter(route_id=route_id)
    
class BusScheduleView(generics.ListAPIView):
    serializer_class = AssignmentSerializer

    def get_queryset(self):
        route_id = self.kwargs['route_id'] 
        return Assignment.objects.filter(route_id=route_id)

class InactiveBusesView(generics.ListAPIView):
    serializer_class = BreakdownSerializer

    def get_queryset(self):
        date = self.kwargs['date']
        return Breakdown.objects.filter(date=date)


class DriverCountByClassView(generics.ListAPIView):
    serializer_class = DriverSerializer

    def get_queryset(self):
        class_name = self.kwargs['class_name']
        return Driver.objects.filter(class_name=class_name)
```