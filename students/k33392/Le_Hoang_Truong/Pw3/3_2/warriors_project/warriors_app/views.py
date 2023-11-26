from rest_framework.response import Response
from django.shortcuts import render
from .serializers import WarriorSerializer,ProfessionCreateSerializer,SkillSerializer
from .models import Warrior,Skill
from rest_framework.decorators import APIView
from rest_framework import generics
# Create your views here.
class WarriorAPIView(APIView):
   def get(self, request):
       warriors = Warrior.objects.all()
       serializer = WarriorSerializer(warriors, many=True)
       return Response({"Warriors": serializer.data})

class WarriorListAPIView(generics.ListAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer


class WarriorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer
    lookup_field = 'id'



class ProfessionCreateView(APIView):

   def post(self, request):
       profession = request.data.get("profession")
       serializer = ProfessionCreateSerializer(data=profession)

       if serializer.is_valid(raise_exception=True):
           profession_saved = serializer.save()

       return Response({"Success": "Profession '{}' created succesfully.".format(profession_saved.title)})

class SkillListView(APIView):
    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response({"Skill" : serializer.data})

    def post(self, request):
        serializer = SkillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Skill" : serializer.data})
        return Response(serializer.errors)