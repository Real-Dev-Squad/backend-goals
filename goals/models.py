from django.db import models


class Goal(models.Model):
    goalType = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    createdAt = models.DateTimeField('date published', auto_now=True)
    createdBy = models.CharField(max_length=50)


class UserGoal(models.Model):
    userId = models.CharField(max_length=50)
    startsOn = models.DateTimeField()
    endsOn = models.DateTimeField()
    percentageCompleted = models.IntegerField(default=0)
    assignedBy = models.CharField(max_length=200)
    status = models.CharField(max_length=50)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
