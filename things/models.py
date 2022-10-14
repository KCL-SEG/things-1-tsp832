from sys import maxsize
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Thing(AbstractBaseUser):
    name = models.CharField(unique = True, max_length = 30, blank = False)
    description = models.CharField(unique = False, max_length = 120, blank = True)
    quantity = models.PositiveSmallIntegerField(unique = False, validators=[MinValueValidator(0), MaxValueValidator(100)])
    USERNAME_FIELD = 'name'
    password = models.TextField(blank = True)
    #REQUIRED_FIELDS = 'name'
    #PASSWORD_FIELD = 'quantity'