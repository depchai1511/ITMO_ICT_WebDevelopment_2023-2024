# main_app/serializers.py
from rest_framework import serializers
from .models import  Bus, BusType, Route, Assignment, Breakdown,Driver


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'
class BusTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusType
        fields = '__all__'

class BusTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusType
        fields = '__all__'

class BusSerializer(serializers.ModelSerializer):
    bus_type = BusTypeSerializer()
    class Meta:
        model = Bus
        fields = ('bus_type','registration_number')

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'

class AssignmentSerializer(serializers.ModelSerializer):
    driver = DriverSerializer()
    bus = BusSerializer()
    route = RouteSerializer()
    class Meta:
        model = Assignment
        fields = '__all__'


class BreakdownSerializer(serializers.ModelSerializer):
    bus = BusSerializer()
    class Meta:
        model = Breakdown
        fields = '__all__'
