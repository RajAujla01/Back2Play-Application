from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.

class WorkoutSession(models.Model):
    workout_num = models.IntegerField()
    exercise_name = models.CharField(max_length=100)
    sets = models.IntegerField()
    reps = models.IntegerField()

    def __str__(self):
        return f"Workout {self.workout_num}: {self.exercise_name}"
    


	
