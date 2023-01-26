from django.contrib import admin
from .models import Routine, Exercise, WorkoutPlan, Set
# Register your models here.

admin.site.register(Routine)
admin.site.register(Exercise)
admin.site.register(WorkoutPlan)
admin.site.register(Set)
