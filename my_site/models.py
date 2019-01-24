from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class User(models.Model):
    name = models.CharField(max_length=35)
    surname = models.CharField(max_length=35)
    role = models.ForeignKey('Role')
    department = models.ForeignKey('Department')

class Role(models.Model):
    name = models.CharField(max_length=35)

class Grade(models.Model):
    name = models.CharField(max_length=35)

class Department(models.Model):
    name = models.CharField(max_length=35)

class Permissions(model.Model):
    code_name = models.CharField(max_length=35)
