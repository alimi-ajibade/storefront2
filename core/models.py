from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# This Class extends (inherits) from the abstract user
# and makes the email field unique


class User(AbstractUser):
    email = models.EmailField(unique=True)
