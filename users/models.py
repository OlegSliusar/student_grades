# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(models.Model):
    class Meta:
        db_table = "user"

    name = models.CharField(max_length=60, default=None)
    surname = models.CharField(max_length=60, default=None)
    fRole = models.ForeignKey('my_site.Role', on_delete=models.DO_NOTHING)
