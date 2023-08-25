from base.base_views import ModelBaseViewSet
from goals.models import Goal
from goals.serializers import GoalSerializer


class GoalViewSet(ModelBaseViewSet):
    queryset = Goal.objects.all().order_by('-created_at')
    serializer_class = GoalSerializer
    filterset_fields = ['status', 'title', 'assigned_to']
