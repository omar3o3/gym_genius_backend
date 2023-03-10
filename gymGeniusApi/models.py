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

# blank=True, null=True, 
class Exercise(models.Model):
    workout_plan = models.ForeignKey(WorkoutPlan, related_name='workout_plan', blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    main_exercise = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name}, {self.main_exercise}"

class Set(models.Model):
    exercise = models.ForeignKey(Exercise, related_name='exercise', on_delete=models.CASCADE)
    reps = models.IntegerField()
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.exercise}"