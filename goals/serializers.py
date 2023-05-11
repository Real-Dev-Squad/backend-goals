from rest_framework_json_api import serializers
from goals.models import Goal

class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ('title', 'description',
                  'created_at', 'created_by', 'assigned_to', 'starts_on', 
                  'ends_on', 'percentage_completed', 'assigned_by', 'status')
