from django.db import models

# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length= 20)
    course_trainer = models.CharField(max_length= 20)
    course_careers = models.CharField(max_length=20)
    course_id = models.PositiveSmallIntegerField(primary_key=True)
    course_description = models.CharField(max_length= 50)
    course_scores = models.PositiveSmallIntegerField()
    course_duration = models.DurationField()
    course_sessions = models.CharField(max_length= 20)
    course_students = models.CharField(max_length= 20)




    def __str__ (self):
        return f"{self.course_name} {self.course_id}"