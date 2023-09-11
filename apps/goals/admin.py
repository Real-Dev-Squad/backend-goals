from django.contrib import admin
from safedelete.admin import SafeDeleteAdmin, highlight_deleted

from apps.goals.models import Goal
# Register your models here.


@admin.register(Goal)
class GoalAdmin(SafeDeleteAdmin):
    list_display = (highlight_deleted, "title", "description", "created_at", "modified_at", "created_by",
                    "assigned_to", "starts_on", "ends_on", "percentage_completed", "assigned_by", "status")
    list_per_page = 25
    list_filter = ("created_at", "modified_at",
                   "starts_on", "ends_on", "status")
    # raw_id_fields = ()
    search_fields = ("title", "created_by", "assigned_to", "assigned_by")
    readonly_fields = ("created_at", "modified_at")
