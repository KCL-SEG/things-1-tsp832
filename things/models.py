from sys import maxsize
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Thing(AbstractUser):
    name = models.CharField(unique = True, max_length = 30, blank = False)
    description = models.TextField(unique = False, max_length = 120, blank = True)
    quantity = models.PositiveSmallIntegerField(unique = False, validators=[MinValueValidator(0), MaxValueValidator(100)])