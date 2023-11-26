# serializers.py
from rest_framework import serializers
from .models import *

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class ProfessionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = '__all__'

class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = '__all__'

class SkillOfWarriorSerializer(serializers.ModelSerializer):
    skill = serializers.StringRelatedField()

    class Meta:
        model = SkillOfWarrior
        fields = '__all__'

class WarriorSerializer(serializers.ModelSerializer):
    profession = ProfessionSerializer()
    warrior_skills = SkillOfWarriorSerializer(many=True, read_only=True)

    class Meta:
        model = Warrior
        fields = '__all__'
    
    def update(self, instance, validated_data):
        profession_data = validated_data.pop('profession', {})
        instance.profession.title = profession_data.get('title', instance.profession.title)
        instance.profession.description = profession_data.get('description', instance.profession.description)
        instance.profession.save()

        instance.name = validated_data.get('name', instance.name)
        instance.level = validated_data.get('level', instance.level)
        instance.race = validated_data.get('race', instance.race)
        instance.save()

        return instance
