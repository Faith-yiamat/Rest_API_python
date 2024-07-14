from django.db import models

# Create your models here.
class Class_period(models.Model):
    start_time = models.DurationField()
    end_time = models.DurationField()
    course = models.CharField()
    classroom = models.CharField()
    day_of_the_week = models.CharField()

    def  __self__(self):
        return f"{self.course}"


   
