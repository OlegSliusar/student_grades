from django.db import models

class Role(models.Model):
    class Meta:
        db_table = "role"
    name = models.CharField(max_length=35)

class Permission(models.Model):
    class Meta:
        db_table = "permission"
    code_name = models.CharField(max_length=35)
