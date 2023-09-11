
from django.contrib import admin
from apps.user.models import User
from safedelete.admin import SafeDeleteAdmin, highlight_deleted


@admin.register(User)
class UserAdmin(SafeDeleteAdmin):
    list_display = ["id", "rds_id", "created_at", "modified_at"]
    search_fields = ('rds_id', 'id')
    ordering = ('created_at', )
