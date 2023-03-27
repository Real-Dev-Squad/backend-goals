from goals.models import Goal, UserGoal
from goals.serializers import GoalSerializer, UserGoalSerialier
from rest_framework import viewsets

class GoalViewSet(viewsets.ModelViewSet):
  queryset = Goal.objects.all()
  serializer_class = GoalSerializer

class UserGoalViewSet(viewsets.ModelViewSet):
  queryset = UserGoal.objects.all()
  serializer_class = UserGoalSerialier