from django.db import models

# Create your models here.
class Class_period(models.Model):
    start_time = models.DurationField()
    end_time = models.DurationField()
    course = models.CharField(max_length= 40)
    classroom = models.CharField(max_length= 40)
    day_of_the_week = models.CharField(max_length= 40)

    def  __self__(self):
        return f"{self.course}"


   
