from django.db import models
from users.models import User

# Create your models here.
class Routine(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class WorkoutPlan(models.Model):
    routine = models.ForeignKey(Routine, related_name='routine', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class Exercise(models.Model):
    workout_plan = models.ForeignKey(WorkoutPlan, related_name='workout_plan', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    main_exercise = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Set(models.Model):
    exercise = models.ForeignKey(Exercise, related_name='exercise', on_delete=models.CASCADE)
    reps = models.IntegerField()
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)