from  rest_framework.views import APIView
from student.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from classPeriod.models import Class_period
from classroom.models import Class
from teacher.models import Teacher
from course.models import Course
from .serializers import ClassperiodSerializer
from .serializers import ClassroomSerializer
from .serializers import  CourseSerializer
from .serializers import  TeacherSerializer
from rest_framework import status
from rest_framework import status


class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = StudentSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


class TeacherListView(APIView):
    def get(self, request):
        teacher = Teacher.objects.all() 
        serializer = TeacherSerializer(teacher, many= True)
        return Response(serializer.data)

    
class ClassroomListView(APIView):
    def get(self, request):
        classroom = Class.objects.all
        serializer = ClassroomSerializer(classroom, many= True)
        return Response(serializer.data)
class CourseListView(APIView):
    def get(self, request):
        course = Course.objects.all() 
        serializer = CourseSerializer(Course , many= True)
        return Response(serializer.data)
class ClassPeriodListView(APIView):
    def get(self, request):
        classperiod = Class_period.objects.all() 
        serializer = ClassperiodSerializer(Course , many= True)
        return Response(serializer.data)
    
class StudentDetailsView(APIView):
    def get(self,request, id):
        student = Student.objects.get(id = id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)  
    def put(self, request, id):
        student = Student.objects.get(id = id) 
        serializer = StudentSerializer(student, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        student = Student.objects.get(id=id)
        student.delete()
        return Response(status= status.HTTP_202_ACCEPTED)
    
     
class TeacherDetailsView(APIView):
    def get(self,request, id):
        teacher = Teacher.objects.get(id = id)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)  
    def put(self, request, id):
        teacher = Teacher.objects.get(id = id) 
        serializer = TeacherSerializer(teacher, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        teacher = Teacher.objects.get(id=id)
        teacher.delete()
        return Response(status= status.HTTP_202_ACCEPTED)  
     
class ClassroomDetailsView(APIView):
    def get(self,request, id):
        classroom = Class.objects.get(id = id)
        serializer = TeacherSerializer(classroom)
        return Response(serializer.data)  
    def put(self, request, id):
        classroom = Class.objects.get(id = id) 
        serializer = TeacherSerializer(classroom, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        classroom = Class.objects.get(id=id)
        classroom.delete()
        return Response(status= status.HTTP_202_ACCEPTED)  
       
class ClassPeriodDetailsView(APIView):
    def get(self,request, id):
        class_period = Class_period.objects.get(id = id)
        serializer = ClassperiodSerializer(class_period)
        return Response(serializer.data)  
    def put(self, request, id):
        class_period = Class_period.objects.get(id = id) 
        serializer = ClassperiodSerializer(class_period, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        class_period = Class_period.objects.get(id=id)
        class_period.delete()
        return Response(status= status.HTTP_202_ACCEPTED)     

class CourseDetailsView(APIView):
    def get(self,request, id):
        course = Course.objects.get(id = id)
        serializer = CourseSerializer(course)
        return Response(serializer.data)  
    def put(self, request, id):
        course = Course.objects.get(id = id) 
        serializer = CourseSerializer(course, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        course = Course.objects.get(id=id)
        course.delete()
        return Response(status= status.HTTP_202_ACCEPTED)   



