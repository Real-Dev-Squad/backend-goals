from apps.base.base_views import ModelBaseViewSet
from apps.goals.models import Goal
from apps.goals.serializers import GoalSerializer
from rest_framework.permissions import IsAuthenticated

from rest_framework_json_api import filters
from rest_framework_json_api import django_filters
from rest_framework.filters import SearchFilter

class GoalViewSet(ModelBaseViewSet):
    queryset = Goal.objects.all().order_by('-created_at')
    serializer_class = GoalSerializer
    filter_backends = [filters.OrderingFilter, SearchFilter, django_filters.DjangoFilterBackend]
    search_fields = ['title']
    filterset_fields = ['status', 'assigned_to']
    # permission_classes = [IsAuthenticated]
