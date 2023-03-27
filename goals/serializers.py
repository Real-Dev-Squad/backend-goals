from rest_framework_json_api import serializers
from goals.models import Goal, UserGoal


class GoalSerializer(serializers.ModelSerializer):
    included_serializers = {
        'usergoal_set': "goals.serializers.UserGoalSerialier",
    }

    class Meta:
        model = Goal
        fields = ('goalType', 'title', 'description',
                  'createdAt', 'createdBy', 'usergoal_set')


class UserGoalSerialier(serializers.ModelSerializer):
    included_serializers = {
        'goal': GoalSerializer,
    }
    class Meta:
        model = UserGoal
        fields = ('userId', 'startsOn', 'endsOn',
                  'percentageCompleted', 'assignedBy', 'status', 'goal')
