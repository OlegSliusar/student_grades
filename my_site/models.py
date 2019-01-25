from django.db import models

class User:
    class Meta:
        db_table = "user"

    Name = models.CharField(max_length=60, default=None)
    Surname = models.CharField(max_length=60, default=None)
    fRole = models.ForeignKey('Role', on_delete=models.DO_NOTHING)
    Department = models.ManyToManyField('Department')

class Role(models.Model):
    class Meta:
        db_table = "role"
    name = models.CharField(max_length=35)

class Grade(models.Model):
    class Meta:
        db_table = "grade"
    name = models.CharField(max_length=35)

class Department(models.Model):
    class Meta:
        db_table = "department"
    name = models.CharField(max_length=35)

class Permission(models.Model):
    class Meta:
        db_table = "permission"
    code_name = models.CharField(max_length=35)

class Step(models.Model):
    class Meta:
        db_table = "step"
    title = models.CharField
