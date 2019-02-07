# users/models.py
from django.db import models

class User(models.Model):
    class Meta:
        db_table = "user"

    name = models.CharField(max_length=60, default=None)
    surname = models.CharField(max_length=60, default=None)
    # fRole = models.ForeignKey('roleaccess.Role', default=None, on_delete=models.CASCADE)
