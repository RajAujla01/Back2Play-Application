from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import WorkoutSession



class WorkoutSessionAdmin(admin.ModelAdmin):
    list_display = ('workout_num', 'exercise_name', 'sets', 'reps')
    list_filter = ('workout_num', 'exercise_name')
    search_fields = ('exercise_name',)

admin.site.register(WorkoutSession, WorkoutSessionAdmin)


