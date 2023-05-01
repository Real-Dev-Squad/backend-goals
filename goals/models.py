from django.db import models


class Goal(models.Model):
    goal_type = models.CharField(max_length=50, blank=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True, default='')
    created_at = models.DateTimeField('date published', auto_now=True)
    created_by = models.CharField(max_length=50, blank=True)


class UserGoal(models.Model):
    user_id = models.CharField(max_length=50)
    starts_on = models.DateTimeField(null=True)
    ends_on = models.DateTimeField(null=True)
    percentage_completed = models.IntegerField(default=0)
    assigned_by = models.CharField(max_length=200, blank=True)
    status = models.CharField(max_length=50, blank=True)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
