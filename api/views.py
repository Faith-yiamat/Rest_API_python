from django.shortcuts import render
from  rest_framework import APIView
from student.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from classPeriod import Class_period
from classroom import Class
from teacher import Teacher
from course import Course
from api.serializers import ClassperiodSerializer, CourseSerializer,ClassroomSerializer,StudentSerializer,TeacherSerializer


class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all
        serializer = StudentSerializer(students, many= True)
        return Response(serializer.data)
class TeacherListViews(APIView):
    def get(self, request):
        teacher = Teacher.objects.all() 
        serializer = TeacherSerializer(teacher, many= True)
        return Response(serializer.data)

    
class ClassroomListView(APIView):
    def get(self, request):
        classroom = Class.objects.all
        serializer = ClassroomSerializer(classroom, many= True)
        return Response(serializer.data)
class CourseListViews(APIView):
    def get(self, request):
        course = Course.objects.all() 
        serializer = CourseSerializer(Course , many= True)
        return Response(serializer.data)
class ClassPeriodListViews(APIView):
    def get(self, request):
        classperiod = Class_period.objects.all() 
        serializer = ClassperiodSerializer(Course , many= True)
        return Response(serializer.data)


