from rest_framework.permissions import IsAuthenticated

from apps.base.base_views import ModelBaseViewSet
from apps.goals.models import Goal
from apps.goals.serializers import GoalSerializer
from apps.base.permissions import AuthorizationPermissions
from apps.base.constants import MEMBER_ROLE


class GoalViewSet(ModelBaseViewSet):
    queryset = Goal.objects.all().order_by('-created_at')
    serializer_class = GoalSerializer
    filterset_fields = ['status', 'title', 'assigned_to']
    # permission_classes = [IsAuthenticated]
