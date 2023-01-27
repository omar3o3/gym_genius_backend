import graphene
from graphene_django import DjangoObjectType
from .models import Routine, Exercise, WorkoutPlan, Set


class RoutineType(DjangoObjectType):
    class Meta:
        model = Routine
        fields = "__all__"

class ExerciseType(DjangoObjectType):
    class Meta:
        model = Exercise
        fields = "__all__"
        # fields = ('id', 'workout_plan', 'name', 'main_exercise', 'created_at')

class WorkoutPlanType(DjangoObjectType):
    class Meta:
        model = WorkoutPlan
        fields = "__all__"
        
class SetType(DjangoObjectType):
    class Meta:
        model = Set
        fields = "__all__"
        
        
        
        
# class ExerciseInput(graphene.InputObjectType):
#     id = graphene.ID()
#     workout_plan = graphene.String()
#     name = graphene.String()
#     main_exercise = graphene.Boolean()
    
    
# class CreateExercise(graphene.Mutation):
#     class Arguments:
#         exercise_data = ExerciseInput(required=True)

#     exercise = graphene.Field(ExerciseType)

#     @staticmethod
#     def mutate(root, info, exercise_data=None):
#         exercise_instance = Exercise( 
#             workout_plan=exercise_data.workout_plan,
#             name=exercise_data.name,
#             main_exercise=exercise_data.main_exercise
#         )
#         exercise_instance.save()
#         return CreateExercise(exercise=exercise_instance)
    
    
# class Mutate(graphene.ObjectType):
#     create_Exercise = graphene.Field(CreateExercise)




        
class Query(graphene.ObjectType):
    all_Routines = graphene.List(RoutineType)
    all_Exercises = graphene.List(ExerciseType)
    all_Workout_Plans = graphene.List(WorkoutPlanType)
    all_Sets = graphene.List(SetType)
    
    
    def resolve_all_Routines(rout, info):
        return Routine.objects.all()

    def resolve_all_Exercises(rout, info):
        return Exercise.objects.all()
    
    # def resolve_all_workoutplans(rout, info):
    def resolve_all_Workout_Plans(rout, info):
        return WorkoutPlan.objects.all()
    
    def resolve_all_Sets(rout, info):
        return Set.objects.all()
    
schema = graphene.Schema(query=Query)