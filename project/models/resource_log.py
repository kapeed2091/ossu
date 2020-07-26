from django.conf import settings
from django.db import models
from project.models import TimeStampMixin, Project


class ResourceLog(TimeStampMixin):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    resource = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.DecimalField(max_digits=5, decimal_places=3)
    description = models.TextField()

    def __str__(self):
        return '{resource_name} entry for Project: {project_name} on {date}'.format(
            resource_name=self.resource.username, project_name=self.project.name, date=self.date)
