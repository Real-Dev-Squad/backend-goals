from rest_framework import serializers
from apps.goals.models import Goal

class GoalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Goal
        fields = ('title', 'description',
                  'created_at', 'created_by', 'assigned_to', 'starts_on', 
                  'ends_on', 'percentage_completed', 'assigned_by', 'status')
