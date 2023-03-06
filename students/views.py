from rest_framework import generics

from students.models import Flow, Direction, Student
from students.serializers import FlowSerializer, DirectionSerializer, StudentSerializer


class FlowListApiView(generics.ListApiView):
    queryset = Flow.objects.all()
    serializer_class = FlowSerializer

class FlowCreateApiView(generics.CreateApiView):
    queryset = Flow.objects.all()
    serializer_class = FlowSerializer


class DirectionListApiView(generics.ListApiView):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer

class DirectionCreateApiView(generics.CreateApiView):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer


class StudentListApiView(generics.ListApiView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentCreateApiView(generics.CreateApiView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDestroyApiView(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer