from goals.models import Goal
from goals.serializers import GoalSerializer
from rest_framework import viewsets

class GoalViewSet(viewsets.ModelViewSet):
  queryset = Goal.objects.all()
  serializer_class = GoalSerializer
