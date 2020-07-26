from django.conf import settings
from django.db import models
from project.models import TimeStampMixin, Project


class ProjectResource(TimeStampMixin):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    resource = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, default='ACTIVE')
