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


