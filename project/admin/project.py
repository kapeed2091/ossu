from django.contrib import admin
from project.models import Project, ProjectResource


class ResourceStackedInline(admin.StackedInline):
    model = ProjectResource
    raw_id_fields = ['project_id', 'resource_id']
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    inlines = [ResourceStackedInline]
