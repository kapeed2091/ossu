from django.contrib import admin
from project.models import ProjectResource


@admin.register(ProjectResource)
class ProjectResourceAdmin(admin.ModelAdmin):
    list_display = ['id', 'project_id', 'project_name', 'resource_id', 'resource_name', 'status']

    def project_name(self, obj):
        return obj.project.name

    def resource_name(self, obj):
        return obj.resource.email
