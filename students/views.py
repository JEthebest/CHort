from rest_framework import generics

from students.models import Flow, Direction, Student
from students.serializers import FlowSerializer, DirectionSerializer, StudentSerializer


class FlowListAPIView(generics.ListAPIView):
    queryset = Flow.objects.all()
    serializer_class = FlowSerializer

class FlowCreateAPIView(generics.CreateAPIView):
    queryset = Flow.objects.all()
    serializer_class = FlowSerializer


class DirectionListAPIView(generics.ListAPIView):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer

class DirectionCreateApiView(generics.CreateAPIView):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer


class StudentListAPIView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentCreateAPIView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDestroyAPIView(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer