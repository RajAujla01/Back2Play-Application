from django.db import models

from embed_video.fields import EmbedVideoField

# Create your models here.



class Library(models.Model):
	exercise_Title = models.CharField(max_length=200)
	exercise_Body = models.TextField()
	exercise_Video = EmbedVideoField()

	class  Meta:
		verbose_name_plural = "Exercises"

	def  __str__(self):
		return  str(self.exercise_Title)
	
