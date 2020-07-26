from django.conf import settings
from django.db import models
from project.models import TimeStampMixin


class Project(TimeStampMixin):
    name = models.CharField(max_length=300)
    resources = models.ManyToManyField(settings.AUTH_USER_MODEL, through='project.ProjectResource')

    def __str__(self):
        return self.name
