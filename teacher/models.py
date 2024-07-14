from django.db import models
from course.models import Course

# Create your models here.

class Teacher(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, default=1)
    first_name = models.CharField(max_length= 20)
    last_name = models.CharField(max_length= 20)
    date_of_birth = models.DateField()
    email = models.EmailField()
    course = models.CharField(max_length= 20)
    gender = models.CharField(max_length= 20)
    id_number = models.PositiveSmallIntegerField()
    years_of_experience = models.PositiveSmallIntegerField()
    nationality = models.CharField(max_length= 20)
    coutry = models.CharField(max_length= 20)
 

    def __self__ (self):
        return f"{self.first_name} {self.last_name}"
