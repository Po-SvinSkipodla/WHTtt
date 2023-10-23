from django.db import models
from django.db.models import SET_NULL


class Team(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Member(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254, unique=True)
    team = models.ForeignKey(to=Team, null=True, on_delete=SET_NULL)

    class Meta:
        unique_together = ("first_name", "last_name",)
