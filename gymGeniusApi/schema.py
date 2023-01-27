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


#FROM YOUTUBE ATTEMPT
#FROM YOUTUBE ATTEMPT
#FROM YOUTUBE ATTEMPT
class ExerciseMutation(graphene.Mutation):
    # print('-'*10)
    class Arguments:
        name = graphene.String()
        main_exercise = graphene.Boolean()
        # workout_plan = graphene.Field(WorkoutPlanType)
        workout_plan = graphene.Int()
    
    exercise = graphene.Field(ExerciseType)
    
    @classmethod
    # def mutate(cls, root, info, name, main_exercise, workout_plan):
    def mutate(cls, root, info, name, main_exercise):
        # workout_plan_obj = WorkoutPlan.objects.find(pk=workout_plan)
        # exercise = Exercise(name=name, main_exercise=main_exercise, workout_plan=workout_plan_obj)
        exercise = Exercise(name=name, main_exercise=main_exercise)
        exercise.save()
        return ExerciseMutation(exercise=exercise)

class Mutation(graphene.ObjectType):
    # create_Exercise = graphene.Field(CreateExercise)
    update_Exercise = ExerciseMutation.Field()
        
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
    
schema = graphene.Schema(query=Query, mutation=Mutation)