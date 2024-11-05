from django.db import models


# create workouts model
class Workout(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    duration_minutes = models.IntegerField()


    def __str__(self):
        return self.name