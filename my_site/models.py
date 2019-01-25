from django.db import models

class Users:
    class Meta:
        db_table = "Users"

        Name = models.CharField(max_length=60, default=None)
        Surname = models.CharField(max_length=60, default=None)
        fRole = models.ForeignKey('RolesModel', on_delete=models.DO_NOTHING)
        Department = models.ManyToManyField('DepartmentsModel')

class Role(models.Model):
    name = models.CharField(max_length=35)

class Grade(models.Model):
    name = models.CharField(max_length=35)

class Department(models.Model):
    name = models.CharField(max_length=35)

class Permissions(models.Model):
    code_name = models.CharField(max_length=35)
