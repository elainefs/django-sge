from django.contrib import admin

from ai.models import AIResult


class AIResultAdmin(admin.ModelAdmin):
    list_display = ("result", "created_at")


admin.site.register(AIResult, AIResultAdmin)
