from django.contrib import admin

from .models import Insight, Team

@admin.register(Insight)
class InsightAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Team)

