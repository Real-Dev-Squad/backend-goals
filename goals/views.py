from goals.models import Goal
from goals.serializers import GoalSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend


class GoalViewSet(viewsets.ModelViewSet):
    queryset = Goal.objects.all().order_by('-created_at')
    serializer_class = GoalSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'title', 'assigned_to']
