from django.db import models
from course.models import Course

# Create your models here.

class Student(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, default=1)
    first_name = models.CharField(max_length= 20)
    last_name = models.CharField(max_length= 20)
    email = models.EmailField()
    country = models.CharField(max_length= 20)
    date_of_birth = models.DateField()
    code = models.PositiveSmallIntegerField()

    def __self__ (self):
        return f"{self.first_name} {self.last_name}"