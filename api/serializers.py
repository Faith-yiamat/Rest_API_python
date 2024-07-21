from rest_framework import serializers
from student.models import Student
from course.models import Course
from teacher.models import Teacher
from  classroom.models import Class
from  classPeriod.models import Class_period

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"   
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = "__all__"        
class ClassperiodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class_period
        fields = "__all__"        
