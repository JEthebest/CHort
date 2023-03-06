from rest_framework import serializers

from students.models import Flow, Direction, Student

class FlowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flow
        fields = (
            'id',
            'title'
        )

class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = (
            'id',
            'title',
            'flow'
        )

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            'id',
            'first_name',
            'last_name',
            'age',
            'direction'
        )