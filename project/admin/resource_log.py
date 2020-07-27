from django.contrib import admin
from project.models import ResourceLog


@admin.register(ResourceLog)
class ResourceLogAdmin(admin.ModelAdmin):
    list_display = ['id', 'project_name', 'resource_name', 'date', 'time', 'description']
    list_filter = ['project__name', 'resource__username']

    def project_name(self, obj):
        return obj.project.name

    def resource_name(self, obj):
        return obj.resource.email
