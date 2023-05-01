from rest_framework_json_api import serializers
from goals.models import Goal, UserGoal


class GoalSerializer(serializers.ModelSerializer):
    included_serializers = {
        'usergoal': "goals.serializers.UserGoalSerialier",
    }

    class Meta:
        model = Goal
        fields = ('goal_type', 'title', 'description',
                  'created_at', 'created_by')


class UserGoalSerialier(serializers.ModelSerializer):
    included_serializers = {
        'goal': GoalSerializer,
    }
    class Meta:
        model = UserGoal
        fields = ('user_id', 'starts_on', 'ends_on',
                  'percentage_completed', 'assigned_by', 'status', 'goal')
