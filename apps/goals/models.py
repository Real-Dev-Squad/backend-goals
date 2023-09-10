from django.db import models

from apps.base.models import BaseModel


class GoalStatusChoices(models.TextChoices):
    ONGOING = "ongoing"
    COMPLETED = "completed"


class Goal(BaseModel):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True, default='')
    created_by = models.CharField(max_length=50, blank=True)
    assigned_to = models.CharField(max_length=50, null=True)
    starts_on = models.DateTimeField(null=True)
    ends_on = models.DateTimeField(null=True)
    percentage_completed = models.IntegerField(default=0)
    assigned_by = models.CharField(max_length=200, blank=True)
    status = models.CharField(max_length=70, choices=GoalStatusChoices.choices, default=GoalStatusChoices.ONGOING)

    def __str__(self) -> str:
        return self.title
