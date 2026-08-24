from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class Cook(AbstractUser):
    years_of_experience = models.PositiveIntegerField(default=0)
