#!/usr/bin/env python
import os
import sys
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_grades.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.TextField()
